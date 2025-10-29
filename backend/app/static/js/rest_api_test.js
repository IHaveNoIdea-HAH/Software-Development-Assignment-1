let session = {};

function getHost() {
    return document.getElementById('host').value;
}

function showSection(section) {
    const content = document.getElementById('content');
    content.innerHTML = '';
    if (section === 'register') {
        content.innerHTML = `
            <h2>Register</h2>
            <input id="reg_username" placeholder="Username"><br>
            <input id="reg_password" type="password" placeholder="Password"><br>
            <input id="reg_email" placeholder="Email"><br>
            <button onclick="registerUser()">Register</button>
            <div id="reg_result"></div>
        `;
    } else if (section === 'login') {
        content.innerHTML = `
            <h2>Login</h2>
            <input id="login_username" placeholder="Username"><br>
            <input id="login_password" type="password" placeholder="Password"><br>
            <button onclick="loginUser()">Login</button>
            <div id="login_result"></div>
        `;
    } else if (section === 'newgame') {
        content.innerHTML = `
            <h2>New Game</h2>
            <select id="difficulty">
                <option>Easy</option>
                <option>Normal</option>
                <option>Hard</option>
            </select><br>
            <button onclick="startGame()">Start Game</button>
            <div id="game_result"></div>
            <div id="crossword_grid"></div>
        `;
    } else if (section === 'guessword') {
        content.innerHTML = `
            <h2>Guess Word</h2>
            <input id="clue_number" type="number" min="1" placeholder="Clue Number"><br>
            <input id="word_guess" placeholder="Word Guess"><br>
            <button onclick="guessWord()">Submit Guess</button>
            <div id="guess_result"></div>
        `;
    } else if (section === 'autosolve') {
        content.innerHTML = `
            <h2>Auto Solve</h2>
            <button onclick="autoSolve()">Auto Solve the Crossword</button>
            <div id="autosolve_result"></div>
            <div id="autosolve_grid"></div>
        `;
    } else if (section === 'solveclue') {
        content.innerHTML = `
            <h2>Solve Clue</h2>
            <input id="solve_clue_number" type="number" min="1" placeholder="Clue Number"><br>
            <button onclick="solveClue()">Solve Clue</button>
            <div id="solveclue_result"></div>
        `;
    }
}

async function registerUser() {
    const username = document.getElementById('reg_username').value;
    const password = document.getElementById('reg_password').value;
    const email = document.getElementById('reg_email').value;
    const url = `${getHost()}/api/user/register`;
    const payload = { username, password, email };
    const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });
    const data = await res.json();
    document.getElementById('reg_result').innerText = JSON.stringify(data);
    if (res.status === 200) {
        session.security_token = data.security_token;
        session.user_id = data.user_id;
        session.username = data.username;
    }
}

async function loginUser() {
    const username = document.getElementById('login_username').value;
    const password = document.getElementById('login_password').value;
    const url = `${getHost()}/api/user/login`;
    const payload = { username, password };
    const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });
    const data = await res.json();
    document.getElementById('login_result').innerText = JSON.stringify(data);
    if (res.status === 200) {
        session.security_token = data.security_token;
        session.user_id = data.user_id;
        session.username = data.username;
    }
}

async function startGame() {
    const difficulty = document.getElementById('difficulty').value.toLowerCase();
    const url = `${getHost()}/api/game/start`;
    const payload = {
        game_difficulty_level: difficulty,
        user_id: session.user_id || -1,
        security_token: session.security_token || ''
    };
    const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });
    const data = await res.json();
    document.getElementById('game_result').innerText = JSON.stringify(data);
    if (res.status === 200) {
        session.game_id = data.game_state.game_id;
        session.crossword = data.crossword;
        renderGrid('crossword_grid', data.crossword.grid);
    }
}

async function guessWord() {
    const clue_number = parseInt(document.getElementById('clue_number').value);
    const word_guess = document.getElementById('word_guess').value;
    const url = `${getHost()}/api/game/guess_word`;
    const payload = {
        clue_number,
        word_guess,
        game_id: session.game_id || -1,
        user_id: session.user_id || -1,
        security_token: session.security_token || ''
    };
    const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });
    const data = await res.json();
    document.getElementById('guess_result').innerText = JSON.stringify(data);
}

async function autoSolve() {
    const url = `${getHost()}/api/game/auto_solve`;
    const payload = {
        game_id: session.game_id || -1,
        user_id: session.user_id || -1,
        security_token: session.security_token || ''
    };
    const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });
    const data = await res.json();
    document.getElementById('autosolve_result').innerText = JSON.stringify(data);
    if (res.status === 200 && data.crossword) {
        renderGrid('autosolve_grid', data.crossword.grid);
    }
}

async function solveClue() {
    const clue_number = parseInt(document.getElementById('solve_clue_number').value);
    const url = `${getHost()}/api/game/solve_clue`;
    const payload = {
        clue_number,
        game_id: session.game_id || -1,
        user_id: session.user_id || -1,
        security_token: session.security_token || ''
    };
    const res = await fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
    });
    const data = await res.json();
    document.getElementById('solveclue_result').innerText = JSON.stringify(data);
}

function renderGrid(elementId, grid) {
    if (!grid) return;
    let html = '<table border="1">';
    for (let row of grid) {
        html += '<tr>';
        for (let cell of row) {
            html += `<td>${cell}</td>`;
        }
        html += '</tr>';
    }
    html += '</table>';
    document.getElementById(elementId).innerHTML = html;
}

