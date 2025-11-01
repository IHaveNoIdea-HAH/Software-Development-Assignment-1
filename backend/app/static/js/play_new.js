// this is to manage the session data stored in localStorage
let session = loadSession() || {};

// Save session data to localStorage
function saveSession() {
  localStorage.setItem('crossword_game', JSON.stringify(session));
}

// Load session data from localStorage
function loadSession() {
  try { return JSON.parse(localStorage.getItem('crossword_game')); }
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

// Main function to start a new game
async function startNewGame(difficulty) {
  difficulty = (difficulty || 'easy').toLowerCase();
  const out = document.getElementById('game_result');
  try {
    const session = window.session || {};
    const data = await fetchJSON('/api/game/start', {
      body: {
        game_difficulty_level: difficulty,
        user_id: session.user_id ?? -1,
        security_token: session.security_token ?? ''
      }
    });
    out.textContent = 'Game started!';
    const grid = data.crossword?.grid || data.grid;
    renderGrid('crossword_grid', grid);
  } catch (err) {
    out.textContent = `Error: ${err.message}`;
  }
}

// Attach event listener to 'New Game' button
window.addEventListener('DOMContentLoaded', function() {
  const btn = document.getElementById('new_game_btn');
  if (btn) btn.addEventListener('click', showDifficultyDialog);
});
