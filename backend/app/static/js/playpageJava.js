function selectDifficulty(level) {
    console.log('Selected difficulty: ' + level);
    // Closes the popup
    document.getElementById('difficultyPopup').classList.remove('active');
    document.getElementById('overlay').style.display = 'none';
   
}

// Show popup when entering the page 
window.addEventListener('load', function() {
    document.getElementById('difficultyPopup').classList.add('active');
    document.getElementById('overlay').style.display = 'block';
});