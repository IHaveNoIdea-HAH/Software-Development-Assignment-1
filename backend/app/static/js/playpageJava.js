// playpageJava.js
// Minimal, battle-tested client for the Crossword play page.
// Expected HTML ids (simple structure):
//  - #difficultyPopup, #overlay
//  - #grid (crossword grid container)
//  - #clues-across, #clues-down (lists)
//  - #game-state (small text area for score/remaining/status)
//  - #guess-form with #clue-number and #clue-guess inputs
//  - optional: buttons in popup call selectDifficulty('easy'|'medium'|'hard')

(() => {
  const API_BASE = "/api";
  let GAME_ID = null;

  // ------- helpers -------
  const $ = (sel) => document.querySelector(sel);
  const el = (tag, cls, text) => {
    const n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  };

  function setStateText(text) {
    const s = $("#game-state");
    if (s) s.textContent = text;
  }

  function message(text, type = "info") {
    // reuse state area if no separate message box exists
    setStateText(text);
  }

  async function post(path, body) {
    const res = await fetch(`${API_BASE}${path}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      credentials: "include",
      body: JSON.stringify(body || {}),
    });
    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(data.message || data.error || `HTTP ${res.status}`);
    return data;
  }

  // ------- difficulty popup (your original logic, tidied) -------
  window.selectDifficulty = async function selectDifficulty(level) {
    console.log("Selected difficulty:", level);

    // Close popup/overlay immediately for snappy feel
    hidePopup();

    try {
      // Try to pass userId if available (falls back to cookie session on server)
      const session = safeJSON(localStorage.getItem("crossword_session")) || {};
      const payload = { difficulty: level, user_id: session.userId };

      message("Starting game…");
      const data = await post("/game/start", payload);

      GAME_ID = data.game_id || data.gameId || null;

      // Defensive shape handling
      const grid = data.grid || data.crossword?.grid || [];
      const clues = data.clues || data.crossword?.clues || { across: [], down: [] };
      const state = data.state || data.game_state || {};

      renderGrid(grid);
      renderClues(clues);
      renderState(state);

      message("Game ready. Good luck!", "success");
    } catch (err) {
      message(`Could not start game: ${err.message}`, "error");
      // Reopen popup so user can try again
      showPopup();
    }
  };

  function showPopup() {
    $("#difficultyPopup")?.classList.add("active");
    const ov = $("#overlay");
    if (ov) ov.style.display = "block";
  }

  function hidePopup() {
    $("#difficultyPopup")?.classList.remove("active");
    const ov = $("#overlay");
    if (ov) ov.style.display = "none";
  }

  // ------- renderers -------
  function renderGrid(grid) {
    const container = $("#grid");
    if (!container) return;
    container.innerHTML = "";

    // Expect grid as 2D array of chars or "#" for blocks
    const table = el("table", "cw-grid");
    grid.forEach((row, r) => {
      const tr = el("tr");
      (row || []).forEach((cell, c) => {
        const td = el("td");
        const isBlock = cell === "#" || cell === null || cell === undefined;
        if (isBlock) {
          td.classList.add("block");
        } else {
          td.classList.add("cell");
          td.setAttribute("data-r", r);
          td.setAttribute("data-c", c);
          td.textContent = typeof cell === "string" && cell.length === 1 ? cell.toUpperCase() : "";
        }
        tr.appendChild(td);
      });
      table.appendChild(tr);
    });
    container.appendChild(table);
  }

  function renderClues(clues) {
    const across = $("#clues-across");
    const down = $("#clues-down");

    if (across) {
      across.innerHTML = "";
      (clues.across || []).forEach((cl) => {
        across.appendChild(renderClueItem(cl));
      });
    }

    if (down) {
      down.innerHTML = "";
      (clues.down || []).forEach((cl) => {
        down.appendChild(renderClueItem(cl));
      });
    }
  }

  function renderClueItem(clue) {
    const li = el("li", "clue-item");
    // Expected fields: number, clue, len/length
    const num = clue.number ?? clue.no ?? "?";
    const text = clue.clue || clue.text || "";
    const len = clue.length ?? clue.len ?? "";
    li.textContent = `${num}. ${text} (${len})`;
    li.dataset.clueNumber = num;
    li.tabIndex = 0; // keyboard focusable
    li.addEventListener("click", () => {
      // Autofill clue number in guess form when clicked
      const inp = $("#clue-number");
      if (inp) { inp.value = num; inp.focus(); }
    });
    return li;
  }

  function renderState(state) {
    const remaining = state.remaining_guesses ?? state.remaining ?? "-";
    const solved = state.solved_words ?? state.solved ?? 0;
    const total = state.total_words ?? state.total ?? "-";
    const score = state.score ?? 0;
    setStateText(`Solved: ${solved}/${total} • Remaining guesses: ${remaining} • Score: ${score}`);

    // win/lose banners
    if (state.status === "won" || state.won === true) {
      message("You won! 🎉", "success");
    } else if (state.status === "lost" || state.lost === true || remaining === 0) {
      message("Out of guesses. Game over.", "error");
    }
  }

  function safeJSON(s) { try { return JSON.parse(s); } catch { return null; } }

  // ------- guess flow -------
  async function handleGuessSubmit(e) {
    e.preventDefault();
    const n = $("#clue-number")?.value?.trim();
    const g = $("#clue-guess")?.value?.trim();

    if (!n || !g) return message("Enter clue number and your guess.", "error");
    if (!GAME_ID) return message("Start a game first.", "error");

    message("Checking guess…");
    try {
      const data = await post("/game/guess_word", {
        game_id: GAME_ID,
        clue_number: Number(n),
        guess: g
      });

      // Update visuals
      if (data.grid || data.crossword?.grid) {
        renderGrid(data.grid || data.crossword.grid);
      }
      if (data.clues || data.crossword?.clues) {
        renderClues(data.clues || data.crossword.clues);
      }
      renderState(data.state || data.game_state || {});

      if (data.correct === true) {
        message("Correct ✅", "success");
        // clear guess field for speed
        if ($("#clue-guess")) $("#clue-guess").value = "";
      } else {
        message(data.message || "Not quite. Try again.", "error");
      }
    } catch (err) {
      message(`Guess failed: ${err.message}`, "error");
    }
  }

  // ------- boot -------
  document.addEventListener("DOMContentLoaded", () => {
    // Show difficulty popup on entry (your original behaviour)
    showPopup();

    // Bind guess form if present
    const gf = $("#guess-form");
    if (gf) gf.addEventListener("submit", handleGuessSubmit);
  });
})();
