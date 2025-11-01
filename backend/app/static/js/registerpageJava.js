// registerpageJava.js
// HTML needed:
// <form id="register-form" data-next="/login?next=/play">
//   <input id="email" name="email">
//   <input id="username" name="username">
//   <input id="password" name="password" type="password">
//   <input id="confirm"  name="confirm"  type="password">
//   <button type="submit">Create account</button>
// </form>
// <div id="register-message"></div>
// <p class="muted">Already have an account?
//   <a id="login-link" href="/login">Login</a>
// </p>

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("register-form");
  const msg  = document.getElementById("register-message");
  const loginLink = document.getElementById("login-link");
  if (!form) return;

  // Load existing session 'crossword-session' from localStorage (if any)
  let session = loadSession() || {};

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = (document.getElementById("email")?.value || "").trim();//added this made here
    const username = (document.getElementById("username")?.value || "").trim();
    const password = (document.getElementById("password")?.value || "");
    const confirm  = (document.getElementById("confirm")?.value  || "");

    // --- Validate the inputs and throw errors if invalid
    if (!email) return show("Email is required!", "error") //added this
    if (!email.endsWith(".com")) return show("Email must end with .com", "error"); //added this
    if (username.length < 3)  return show("Username must be ≥ 3 characters.", "error");
    if (password.length < 6)  return show("Password must be ≥ 6 characters.", "error");
    if (password !== confirm) return show("Passwords do not match.", "error");

    show("Creating your account…");

    try {
      const res = await fetch("/api/user/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({email,  username, password }),
      });

      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.message || data.error || " New user registration failed.");

      // We prefer auto-login, let's store session here
      session.security_token = data.security_token;
      session.user_id        = data.user_id;
      session.username       = data.username;
      session.last_result    = data.result;
      session.last_message   = data.message;

      // Save session to localStorage for future use in /play etc.
      saveSession(session);

      // Now we are good to go straightaway to /play and avoid extra login step, so better user experience overall
      show("Account created! Redirecting to play…", "success");
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
    msg.className = `msg ${type}`;
  }

  function getNext(formEl) {
    const urlNext = new URLSearchParams(window.location.search).get("next");
    return urlNext || formEl?.dataset?.next || null;
  }

});
