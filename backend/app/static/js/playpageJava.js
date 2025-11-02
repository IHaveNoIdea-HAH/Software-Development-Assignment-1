// this is to manage the session data stored in localStorage
let session = loadSession() || {};

// Save session data to localStorage
function saveSession(s) {
  localStorage.setItem('crossword_session', JSON.stringify(s));
}

// Load session data from localStorage
function loadSession() {
  try { return JSON.parse(localStorage.getItem('crossword_session')); }
  catch { return null; }
}


// Helper to make a POST request and parse JSON
async function fetchJSON(url, { body }) {
  const resp = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    credentials: 'include',
    body: JSON.stringify(body)
  });
  if (!resp.ok) throw new Error(await resp.text());
  return await resp.json();
}


// Render crossword grid into a container
function renderGrid(containerId, grid) {
  const container = document.getElementById(containerId);
  if (!container || !Array.isArray(grid)) return;
  container.innerHTML = '';
  const table = document.createElement('table');
  table.className = 'crossword-table';
  for (const row of grid) {
    const tr = document.createElement('tr');
    for (const cell of row) {
      const td = document.createElement('td');
      td.textContent = cell === null ? '' : cell;
      td.className = cell === null ? 'empty-cell' : 'filled-cell';
      tr.appendChild(td);
    }
    table.appendChild(tr);
  }
  container.appendChild(table);
}

// Render crossword clues into the clues_container
function renderClues(clues) {
  const container = document.getElementById('clues_container');
  if (!container) return;
  container.innerHTML = '';
  if (!Array.isArray(clues) || clues.length === 0) {
    container.textContent = 'No clues available.';
    return;
  }
  // Group clues by direction
  const grouped = clues.reduce((acc, clue) => {
    (acc[clue.direction] = acc[clue.direction] || []).push(clue);
    return acc;
  }, {});
  for (const dir of ['across', 'down']) {
    if (grouped[dir]) {
      const dirTitle = document.createElement('h3');
      dirTitle.textContent = dir.charAt(0).toUpperCase() + dir.slice(1);
      container.appendChild(dirTitle);
      const ul = document.createElement('ul');
      grouped[dir].forEach(clue => {
        const li = document.createElement('li');
        li.textContent = `${clue.number}. ${clue.text}`;
        ul.appendChild(li);
      });
      container.appendChild(ul);
    }
  }
}

// Show difficulty selection dialog and start game after selection
function showDifficultyDialog() {
  // Remove any existing dialog
  document.getElementById('difficulty-dialog')?.remove();

  // Create dialog container
  const dialog = document.createElement('div');
  dialog.id = 'difficulty-dialog';
  dialog.style.position = 'fixed';
  dialog.style.top = '0';
  dialog.style.left = '0';
  dialog.style.width = '100vw';
  dialog.style.height = '100vh';
  dialog.style.background = 'rgba(0,0,0,0.4)';
  dialog.style.display = 'flex';
  dialog.style.alignItems = 'center';
  dialog.style.justifyContent = 'center';
  dialog.style.zIndex = '9999';

  // Dialog content
  dialog.innerHTML = `
    <div style="background:white;padding:32px 24px;border-radius:8px;box-shadow:0 2px 16px #0003;min-width:320px;text-align:center;">
      <h2>Select Game Difficulty</h2>
      <p>Please choose a difficulty level:</p>
      <button class="diff-btn" data-diff="easy">Easy<br><span style='font-size:12px'>(5 words, 30 guess limit)</span></button><br><br>
      <button class="diff-btn" data-diff="normal">Normal<br><span style='font-size:12px'>(10 words, 20 guess limit)</span></button><br><br>
      <button class="diff-btn" data-diff="hard">Hard<br><span style='font-size:12px'>(15 words, 20 guess limit)</span></button><br><br>
      <button id="cancel-diff" style="margin-top:10px;">Cancel</button>
    </div>
  `;

  document.body.appendChild(dialog);

  // Handle selection
  dialog.querySelectorAll('.diff-btn').forEach(btn => {
    btn.onclick = function() {
      const diff = btn.getAttribute('data-diff');
      dialog.remove();
      startNewGame(diff);
    };
  });
  dialog.querySelector('#cancel-diff').onclick = function() {
    dialog.remove();
  };
}

// Fill the clue number dropdown with numbers equal to the count of clues
function fillClueDropdown(clues) {
  const select = document.getElementById('clue_number_select');
  if (!select) return;
  // Remove all options except the first (placeholder)
  select.innerHTML = '<option value="" disabled selected>Select Clue Number</option>';
  if (!Array.isArray(clues) || clues.length === 0) return;
  for (let i = 1; i <= clues.length; i++) {
    const opt = document.createElement('option');
    opt.value = i;
    opt.textContent = i;
    select.appendChild(opt);
  }
}

// Render game state into the game_state container
function renderGameState(state) {
  const container = document.getElementById('game_state');
  if (!container) return;
  container.innerHTML = '';
  if (!state || typeof state !== 'object') {
    container.textContent = 'No game state available.';
    return;
  }
  // Create a table for game state
  const table = document.createElement('table');
  table.className = 'game-state-table';
  const rows = [
    // ['Status', state.game_status],
    ['Game Result', state.game_result ?? 'In Progress'],
    ['Game Score', state.current_score],
    ['Guess Limit', state.guess_limit],
    ['Guesses Made', state.guesses_made],
    ['Guesses Left', state.guesses_left],
    ['Words Solved', state.words_solved],
    ['Words To Solve', state.words_to_solve]
  ];
  for (const [label, value] of rows) {
    const tr = document.createElement('tr');
    const tdLabel = document.createElement('td');
    tdLabel.textContent = label;
    tdLabel.style.fontWeight = 'bold';
    const tdValue = document.createElement('td');
    tdValue.textContent = value;
    tr.appendChild(tdLabel);
    tr.appendChild(tdValue);
    table.appendChild(tr);
  }
  container.appendChild(table);
}

// Main function to start a new game
async function startNewGame(difficulty) {
  difficulty = (difficulty || 'normal').toLowerCase();
  const out = document.getElementById('status_message');
  try {
   const res = await fetch("/api/game/start", {
     method: "POST",
     headers: { "Content-Type": "application/json" },
     credentials: "include",
     body: JSON.stringify({
       game_difficulty_level: difficulty,
       user_id: session.user_id ?? -1,
       security_token: session.security_token ?? ''
     }),
   });

   const data = await res.json().catch(() => ({}));
   if (!res.ok) throw new Error(data.message || data.error || "Starting new game failed.");


    out.textContent = data.message;

    // Store game ID in session
    session.game_id = data.game_state?.game_id;
    session.last_result    = data.result;
    session.last_message   = data.message;

    // Update session data
    saveSession(session);

    // Here we add more rendering logic here for clues, state, etc.
    // Render the crossword grid
    const grid = data.crossword?.grid;
    renderGrid('crossword_grid', grid);
    // Fill clue dropdown
    fillClueDropdown(data.crossword?.clues);
    // Render clues
    renderClues(data.crossword?.clues);
    // Render game state
    renderGameState(data.game_state);
    // render the game state onto the HUD
  } catch (err) {
    out.textContent = `Error: ${err.message}`;
  }
}

// Check if a game is in progress and confirm before starting a new one
function checkAndStartNewGame() {
  const session = loadSession() || {};
  if (session.game_id) {
    // Show confirmation dialog
    const dialog = document.createElement('div');
    dialog.id = 'confirm-new-game-dialog';
    dialog.style.position = 'fixed';
    dialog.style.top = '0';
    dialog.style.left = '0';
    dialog.style.width = '100vw';
    dialog.style.height = '100vh';
    dialog.style.background = 'rgba(0,0,0,0.4)';
    dialog.style.display = 'flex';
    dialog.style.alignItems = 'center';
    dialog.style.justifyContent = 'center';
    dialog.style.zIndex = '10000';
    dialog.innerHTML = `
      <div style="background:white;padding:32px 24px;border-radius:8px;box-shadow:0 2px 16px #0003;min-width:320px;text-align:center;">
        <h2>Current Game In Progress</h2>
        <p>You have an unfinished game. Would you like to finish it or start a new one?</p>
        <button id="confirm-new-game">Start New Game</button>
        <button id="cancel-new-game" style="margin-left:20px;">Cancel</button>
      </div>
    `;
    document.body.appendChild(dialog);
    document.getElementById('confirm-new-game').onclick = function() {
      dialog.remove();
      showDifficultyDialog();
    };
    document.getElementById('cancel-new-game').onclick = function() {
      dialog.remove();
    };
  } else {
    showDifficultyDialog();
  }
}

// Check if user is logged in; if not, show dialog and redirect to /login
function checkUserLoggedIn() {
  const session = loadSession() || {};
  if (!session.user_id || !session.security_token) {
    // Show dialog
    const dialog = document.createElement('div');
    dialog.id = 'login-required-dialog';
    dialog.style.position = 'fixed';
    dialog.style.top = '0';
    dialog.style.left = '0';
    dialog.style.width = '100vw';
    dialog.style.height = '100vh';
    dialog.style.background = 'rgba(0,0,0,0.4)';
    dialog.style.display = 'flex';
    dialog.style.alignItems = 'center';
    dialog.style.justifyContent = 'center';
    dialog.style.zIndex = '10000';
    dialog.innerHTML = `
      <div style="background:white;padding:32px 24px;border-radius:8px;box-shadow:0 2px 16px #0003;min-width:320px;text-align:center;">
        <h2>Login Required</h2>
        <p>You need to login first!</p>
        <button id="login-redirect-btn">Go to Login</button>
      </div>
    `;
    document.body.appendChild(dialog);
    document.getElementById('login-redirect-btn').onclick = function() {
      window.location.href = '/login';
    };
    // Also auto-redirect after 2 seconds
    setTimeout(function() {
      window.location.href = '/login';
    }, 10000);
    return false;
  }
  return true;
}


// Handle guess word submission
async function submitGuessWord() {
  const session = loadSession() || {};
  const userId = session.user_id;
  const token = session.security_token;
  const gameId = session.game_id;
  const wordGuess = document.getElementById('word_guess_user_input')?.value?.trim();
  const clueNumber = document.getElementById('clue_number_select')?.value;
  const statusMsg = document.getElementById('status_message');

  // Basic inputs validation to ensure we send good info to backend
  if (!userId || !token || !gameId) {
    statusMsg.textContent = 'Session missing. Please login and start a game.';
    return;
  }
  if (!wordGuess) {
    statusMsg.textContent = 'Please enter a guess word.';
    return;
  }
  if (!clueNumber) {
    statusMsg.textContent = 'Please select a clue number.';
    return;
  }

  try {
    const res = await fetch('/api/game/guess_word', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify({
        user_id: userId,
        security_token: token,
        game_id: gameId,
        word_guess: wordGuess,
        clue_number: Number(clueNumber)
      })
    });

    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(data.message || data.error || 'Word guessing failed.');

    statusMsg.textContent = data.message || 'Guess submitted!';

    // Show dialog based on correctness of the guess made by the player
    if (typeof data.is_correct !== 'undefined') {
      const dialog = document.createElement('div');
      dialog.id = 'guess-result-dialog';
      dialog.style.position = 'fixed';
      dialog.style.top = '0';
      dialog.style.left = '0';
      dialog.style.width = '100vw';
      dialog.style.height = '100vh';
      dialog.style.background = 'rgba(0,0,0,0.4)';
      dialog.style.display = 'flex';
      dialog.style.alignItems = 'center';
      dialog.style.justifyContent = 'center';
      dialog.style.zIndex = '10000';
      let msg = '';
      if (data.is_correct) {
        msg = `<h2>Correct Guess for word <span style='color:green'>${data.answer}</span></h2><p>${data.points_scored} points scored</p>`;
      } else {
        msg = `<h2>Ooops, your guess was wrong, try again!</h2>`;
      }
      dialog.innerHTML = `<div style='background:white;padding:32px 24px;border-radius:8px;box-shadow:0 2px 16px #0003;min-width:320px;text-align:center;'>${msg}<br><button id='close-guess-dialog'>OK</button></div>`;
      document.body.appendChild(dialog);
      document.getElementById('close-guess-dialog').onclick = function() {
        dialog.remove();
      };
      // Optionally auto-close after 10 seconds
      setTimeout(() => { dialog.remove(); }, 10000);
    }

    // Let's update the game state to show the latest info
    if (data.game_state) renderGameState(data.game_state);

    // here we render the crossword grid again to show any updates sent by backend
    if (data.crossword?.grid) renderGrid('crossword_grid', data.crossword.grid);

    // Clear the inputs after word guess has been submitted
    document.getElementById('word_guess_user_input').value = '';
    document.getElementById('clue_number_select').value = '';
  } catch (err) {
    statusMsg.textContent = `Error: ${err.message}`;
  }
}


// Handle solve clue submission
async function submitSolveClue() {
  const session = loadSession() || {};
  const userId = session.user_id;
  const token = session.security_token;
  const gameId = session.game_id;
  const clueNumber = document.getElementById('clue_number_select')?.value;
  const statusMsg = document.getElementById('status_message');

  // Basic inputs validation to ensure we send good info to backend
  if (!userId || !token || !gameId) {
    statusMsg.textContent = 'Session missing. Please login and start a game.';
    return;
  }
  if (!clueNumber) {
    statusMsg.textContent = 'Please select a clue number.';
    return;
  }

  try {
    const res = await fetch('/api/game/solve_clue', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify({
        user_id: userId,
        security_token: token,
        game_id: gameId,
        clue_number: Number(clueNumber)
      })
    });

    const data = await res.json().catch(() => ({}));
    if (!res.ok) throw new Error(data.message || data.error || 'Solving clue failed.');

    statusMsg.textContent = data.message || 'Solve clue submitted!';

    // Show dialog based on correctness of the guess made by the player
    if (data.result == 'success') {
      const dialog = document.createElement('div');
      dialog.id = 'guess-result-dialog';
      dialog.style.position = 'fixed';
      dialog.style.top = '0';
      dialog.style.left = '0';
      dialog.style.width = '100vw';
      dialog.style.height = '100vh';
      dialog.style.background = 'rgba(0,0,0,0.4)';
      dialog.style.display = 'flex';
      dialog.style.alignItems = 'center';
      dialog.style.justifyContent = 'center';
      dialog.style.zIndex = '10000';
      let msg = '';
      msg = `<h2>Clue solved, answer is <span style='color:red'>${data.answer}</span></h2><p>${data.penalty_points} penalty points scored</p>`;
      dialog.innerHTML = `<div style='background:white;padding:32px 24px;border-radius:8px;box-shadow:0 2px 16px #0003;min-width:320px;text-align:center;'>${msg}<br><button id='close-guess-dialog'>OK</button></div>`;
      document.body.appendChild(dialog);
      document.getElementById('close-guess-dialog').onclick = function() {
        dialog.remove();
      };
      // Optionally auto-close after 10 seconds
      setTimeout(() => { dialog.remove(); }, 10000);
    }

    // Let's update the game state to show the latest info
    if (data.game_state) renderGameState(data.game_state);

    // here we render the crossword grid again to show any updates sent by backend
    if (data.crossword?.grid) renderGrid('crossword_grid', data.crossword.grid);

    // Clear the inputs after word guess has been submitted
    document.getElementById('word_guess_user_input').value = '';
    document.getElementById('clue_number_select').value = '';
  } catch (err) {
    statusMsg.textContent = `Error: ${err.message}`;
  }
}


// Attach event listener to 'New Game' button
window.addEventListener('DOMContentLoaded', function() {
  if (!checkUserLoggedIn()) return;
  const btn = document.getElementById('new_game_btn');
  if (btn) btn.addEventListener('click', checkAndStartNewGame);
  const guessBtn = document.getElementById('submit_guess_word_btn');
  if (guessBtn) guessBtn.addEventListener('click', submitGuessWord);
  const solveClueBtn = document.getElementById('submit_solve_clue_btn');
  if (solveClueBtn) solveClueBtn.addEventListener('click', submitSolveClue);
});
