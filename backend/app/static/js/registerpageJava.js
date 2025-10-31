// registerpageJava.js
// HTML needed:
// <form id="register-form" data-next="/login?next=/play">
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

  // --- Keep the login link smart: /login?next=/play (or preserved ?next=)
  const desiredNext = new URLSearchParams(window.location.search).get("next") || "/play";
  if (loginLink) {
    const target = `/login?next=${encodeURIComponent(desiredNext)}`;
    loginLink.setAttribute("href", target);
    loginLink.addEventListener("click", (e) => {
      e.preventDefault();
      window.location.href = target;
    });
  }

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const username = (document.getElementById("username")?.value || "").trim();
    const password = (document.getElementById("password")?.value || "");
    const confirm  = (document.getElementById("confirm")?.value  || "");

    if (username.length < 3)  return show("Username must be ≥ 3 characters.", "error");
    if (password.length < 6)  return show("Password must be ≥ 6 characters.", "error");
    if (password !== confirm) return show("Passwords do not match.", "error");

    show("Creating your account…");

    try {
      const res = await fetch("/api/user/register", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        credentials: "include",
        body: JSON.stringify({ username, password }),
      });

      const data = await res.json().catch(() => ({}));
      if (!res.ok) throw new Error(data.message || data.error || "Registration failed.");

      show("Account created! Redirecting to login…", "success");
      window.location.href = getNext(form) || `/login?next=${encodeURIComponent(desiredNext)}`;

      // If you prefer auto-login, you can store session here and go to /play instead.
    } catch (err) {
      show(String(err.message || err), "error");
    }
  });

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
