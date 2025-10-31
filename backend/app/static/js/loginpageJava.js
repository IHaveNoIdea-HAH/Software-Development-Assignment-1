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

  // If already logged in, send straight to play (nice UX).
  const existing = safeJSON(localStorage.getItem("crossword_session"));
  if (existing?.userId) {
    window.location.href = getNext(form) || "/play";
    return;
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = (document.getElementById("username")?.value || "").trim();
    const password = (document.getElementById("password")?.value || "");

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

      // Store minimal session for later pages (no secrets)
      localStorage.setItem(
        "crossword_session",
        JSON.stringify({
          userId: data.user?.id,
          username: data.user?.username || username,
          at: Date.now(),
        })
      );

      show("Success! Redirecting…", "success");
      window.location.href = getNext(form) || "/play";
    } catch (err) {
      show(String(err.message || err), "error");
    }
  });

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



