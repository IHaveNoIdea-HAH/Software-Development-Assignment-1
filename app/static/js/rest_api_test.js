// Manual tester for REST API to test various end points using JavaScript code.

let session = loadSession() || {};

// ---- helpers ----
function getHost() {
  // Prefer same-origin during local dev to avoid CORS
  const input = document.getElementById('host')?.value?.trim() || '';
  if (!input) return ''; // use relative paths => same-origin

  try {
    const target = new URL(input);
    const cur = new URL(window.location.origin);

    // If both are loopback and only differ in hostname, use same-origin
    const loopbacks = new Set(['localhost', '127.0.0.1']);
    const samePort = (target.port || (target.protocol === 'https:' ? '443' : '80')) === (cur.port || (cur.protocol === 'https:' ? '443' : '80'));
    if (loopbacks.has(target.hostname) && loopbacks.has(cur.hostname) && samePort && target.protocol === cur.protocol) {
      return ''; // same-origin avoids CORS with credentials
    }

    return target.origin.replace(/\/+$/, '');
  } catch {
    return input.replace(/\/+$/, '');
  }
}

function saveSession() {
  localStorage.setItem('rest_api_session', JSON.stringify(session));
}
function loadSession() {
  try { return JSON.parse(localStorage.getItem('rest_api_session')); }
  catch { return null; }
}

async function fetchJSON(path, { method = 'POST', body = {}, headers = {} } = {}) {
  const url = `${getHost()}${path}`;
  const res = await fetch(url, {
    method,
    headers: { 'Content-Type': 'application/json', ...headers },
    credentials: 'include',             // allow Flask session cookies
    body: method === 'GET' ? undefined : JSON.stringify(body),
  });
  let data = null;
  try { data = await res.json(); } catch (_) { /* non-JSON */ }
  if (!res.ok) {
    const msg = (data && (data.message || data.error)) || `HTTP ${res.status}`;
    throw new Error(msg);
  }
  return data ?? {};
}

function showSection(section) {
  const content = document.getElementById('content');
  if (!content) return;
  content.innerHTML = '';

  const views = {
    register: `
      <h2>Register</h2>
      <input id="reg_username" placeholder="Username"><br>
      <input id="reg_password" type="password" placeholder="Password"><br>
      <input id="reg_email" placeholder="Email (optional)"><br>
      <button id="btn_register">Register</button>
      <pre id="reg_result" class="result"></pre>
    `,
    login: `
      <h2>Login</h2>
      <input id="login_username" placeholder="Username"><br>
      <input id="login_password" type="password" placeholder="Password"><br>
      <button id="btn_login">Login</button>
      <pre id="login_result" class="result"></pre>
    `,
    newgame: `
      <h2>New Game</h2>
      <select id="difficulty">
        <option>easy</option><option>normal</option><option>hard</option>
      </select><br>
      <button id="btn_start">Start Game</button>
      <pre id="game_result" class="result"></pre>
      <div id="crossword_grid"></div>
    `,
    guessword: `
      <h2>Guess Word</h2>
      <input id="clue_number" type="number" min="1" placeholder="Clue Number"><br>
      <input id="word_guess" placeholder="Your Guess"><br>
      <button id="btn_guess">Submit Guess</button>
      <pre id="guess_result" class="result"></pre>
    `,
    autosolve: `
      <h2>Auto Solve</h2>
      <button id="btn_autosolve">Auto Solve the Crossword</button>
      <pre id="autosolve_result" class="result"></pre>
      <div id="autosolve_grid"></div>
    `,
    solveclue: `
      <h2>Solve Clue (penalty)</h2>
      <input id="solve_clue_number" type="number" min="1" placeholder="Clue Number"><br>
      <button id="btn_solveclue">Solve Clue</button>
      <pre id="solveclue_result" class="result"></pre>
    `
  };

  content.innerHTML = views[section] || '<p>Unknown section</p>';

  // bind buttons
  if (section === 'register') document.getElementById('btn_register')?.addEventListener('click', registerUser);
  if (section === 'login')    document.getElementById('btn_login')?.addEventListener('click', loginUser);
  if (section === 'newgame')  document.getElementById('btn_start')?.addEventListener('click', startGame);
  if (section === 'guessword')document.getElementById('btn_guess')?.addEventListener('click', guessWord);
  if (section === 'autosolve')document.getElementById('btn_autosolve')?.addEventListener('click', autoSolve);
  if (section === 'solveclue')document.getElementById('btn_solveclue')?.addEventListener('click', solveClue);
}

// ---- actions ----
async function registerUser() {
  const username = document.getElementById('reg_username')?.value?.trim() || '';
  const password = document.getElementById('reg_password')?.value || '';
  const email    = document.getElementById('reg_email')?.value?.trim() || undefined;

  const out = document.getElementById('reg_result');
  try {
    const data = await fetchJSON('/api/user/register', {
      body: { username, password, email }
    });
    out.textContent = JSON.stringify(data, null, 2);

    // If backend returns these, store them; otherwise skip gracefully.
    session.security_token = data.security_token ?? session.security_token;
    session.user_id        = data.user_id ?? data.user?.id ?? session.user_id;
    session.username       = data.username ?? data.user?.username ?? username;
    saveSession();
  } catch (err) {
    out.textContent = `Error: ${err.message}`;
  }
}

async function loginUser() {
  const username = document.getElementById('login_username')?.value?.trim() || '';
  const password = document.getElementById('login_password')?.value || '';
  const out = document.getElementById('login_result');

  try {
    const data = await fetchJSON('/api/user/login', { body: { username, password } });
    out.textContent = JSON.stringify(data, null, 2);

    session.security_token = data.security_token ?? session.security_token;
    session.user_id        = data.user_id ?? data.user?.id ?? session.user_id;
    session.username       = data.username ?? data.user?.username ?? username;
    saveSession();
  } catch (err) {
    out.textContent = `Error: ${err.message}`;
  }
}

async function startGame() {
  const difficulty = (document.getElementById('difficulty')?.value || 'easy').toLowerCase();
  const out = document.getElementById('game_result');

  try {
    const data = await fetchJSON('/api/game/start', {
      body: {
        game_difficulty_level: difficulty,     // keep your existing field name
        user_id: session.user_id ?? -1,
        security_token: session.security_token ?? ''
      }
    });
    out.textContent = JSON.stringify(data, null, 2);

    // store ids/state defensively
    session.game_id  = data.game_state?.game_id ?? data.state?.game_id ?? session.game_id;
    session.crossword = data.crossword ?? session.crossword;
    saveSession();

    const grid = data.crossword?.grid || data.grid;
    renderGrid('crossword_grid', grid);
  } catch (err) {
    out.textContent = `Error: ${err.message}`;
  }
}

async function guessWord() {
  const clue_number = parseInt(document.getElementById('clue_number')?.value || '0', 10);
  const guess       = document.getElementById('word_guess')?.value?.trim() || '';
  const out = document.getElementById('guess_result');

  try {
    const data = await fetchJSON('/api/game/guess_word', {
      body: {
        clue_number,
        guess,                        // <-- rename to word_guess if your backend needs that
        game_id: session.game_id ?? -1,
        user_id: session.user_id ?? -1,
        security_token: session.security_token ?? ''
      }
    });
    out.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    out.textContent = `Error: ${err.message}`;
  }
}

async function autoSolve() {
  const out = document.getElementById('autosolve_result');
  try {
    const data = await fetchJSON('/api/game/auto_solve', {
      body: {
        game_id: session.game_id ?? -1,
        user_id: session.user_id ?? -1,
        security_token: session.security_token ?? ''
      }
    });
    out.textContent = JSON.stringify(data, null, 2);
    const grid = data.crossword?.grid || data.grid;
    renderGrid('autosolve_grid', grid);
  } catch (err) {
    out.textContent = `Error: ${err.message}`;
  }
}

async function solveClue() {
  const clue_number = parseInt(document.getElementById('solve_clue_number')?.value || '0', 10);
  const out = document.getElementById('solveclue_result');
  try {
    const data = await fetchJSON('/api/game/solve_clue', {
      body: {
        clue_number,
        game_id: session.game_id ?? -1,
        user_id: session.user_id ?? -1,
        security_token: session.security_token ?? ''
      }
    });
    out.textContent = JSON.stringify(data, null, 2);
  } catch (err) {
    out.textContent = `Error: ${err.message}`;
  }
}

// ---- rendering ----
function escapeHTML(s) {
  return String(s ?? '')
    .replace(/&/g, '&amp;').replace(/</g, '&lt;')
    .replace(/>/g, '&gt;').replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function renderGrid(elementId, grid) {
  const mount = document.getElementById(elementId);
  if (!mount || !Array.isArray(grid)) return;

  let html = '<table class="cw-grid" border="1" cellspacing="0" cellpadding="4">';
  for (const row of grid) {
    html += '<tr>';
    for (const cell of (row || [])) {
      const isBlock = cell === '#' || cell === null || cell === undefined;
      html += isBlock
        ? '<td class="block">#</td>'
        : `<td class="cell">${escapeHTML(typeof cell === 'string' ? cell.toUpperCase() : cell)}</td>`;
    }
    html += '</tr>';
  }
  html += '</table>';
  mount.innerHTML = html;
}
