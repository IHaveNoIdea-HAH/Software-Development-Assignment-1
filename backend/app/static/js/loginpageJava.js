// loginpageJava.js
// HTML needed:
// <form id="login-form" data-next="/play">
//   <input id="username" name="username">
//   <input id="password" name="password" type="password">
//   <button type="submit">Login</button>
// </form>
// <div id="login-message"></div>

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("login-form");
  const msg  = document.getElementById("login-message");
  if (!form) return;

  // Load existing session 'crossword-session' from localStorage (if any)
  let session = loadSession() || {};

  // If already logged in, send straight to play (nice UX).
  if (session?.user_id) {
    window.location.href = getNext(form) || "/play";
    return;
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = (document.getElementById("username")?.value || "").trim();
    const password = (document.getElementById("password")?.value || "");

    // --- Validate the inputs and throw errors if invalid
    if (username.length < 3 || password.length < 6) {
      return show("Username must be ≥ 3 and password ≥ 6.", "error");
    }

    show("Signing in…");

    try {
      const res = await fetch("/api/user/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({ username, password }),
      });

      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.message || data.error || "Login failed.");

      session.security_token = data.security_token;
      session.user_id        = data.user_id;
      session.username       = data.username;
      session.last_result    = data.result;
      session.last_message   = data.message;

      // If game state returned, save that too so when the /play page is loaded it fetches the in-progress game from the session.
      if(data.game_state) {
          session.game_id = data.game_state?.game_id;
          session.game_state    = data.game_state;
          session.game_status   = data.game_state?.game_status;
          session.crossword     = data.crossword;
      }

      // Save session to localStorage for future use in /play etc.
      saveSession(session);

      show("Success! Redirecting…", "success");
      window.location.href = getNext(form) || "/play";
    } catch (err) {
      show(String(err.message || err), "error");
    }
  });

  // Save session data to localStorage
  function saveSession(s) {
    localStorage.setItem('crossword_session', JSON.stringify(s));
  }

  // Load session data from localStorage
  function loadSession() {
    try { return JSON.parse(localStorage.getItem('crossword_session')); }
    catch { return null; }
  }

  function show(text, type = "info") {
    if (!msg) return;
    msg.textContent = text;
    msg.className = `msg ${type}`; // style via .msg.info/.success/.error
  }

  function getNext(formEl) {
    // priority: URL ?next=/path  →  form data-next  → null
    const urlNext = new URLSearchParams(window.location.search).get("next");
    return urlNext || formEl?.dataset?.next || null;
  }

  function safeJSON(s) {
    try { return JSON.parse(s); } catch { return null; }
  }
});



