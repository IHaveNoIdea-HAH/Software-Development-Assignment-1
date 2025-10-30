/* Function to open instructions popup */
function openInstructionsPopup() {
    document.getElementById('instructionsPopup').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
}

/* Function to open difficulty popup */
function openDifficultyPopup() {
    document.getElementById('difficultyPopup').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
}

/* Function to close all popups */
function closeAllPopups() {
    document.getElementById('instructionsPopup').style.display = 'none';
    document.getElementById('difficultyPopup').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
}