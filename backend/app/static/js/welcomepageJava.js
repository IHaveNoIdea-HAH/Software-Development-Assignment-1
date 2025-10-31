// welcomepageJava.js (compact)
const $ = (id) => document.getElementById(id);
const overlay = $('overlay');
const POPUPS = ['instructionsPopup', 'difficultyPopup'];

function open(id) {
  const p = $(id);
  if (!p) return;
  p.style.display = 'block';
  if (overlay) overlay.style.display = 'block';
}
function closeAll() {
  POPUPS.forEach(i => { const p = $(i); if (p) p.style.display = 'none'; });
  if (overlay) overlay.style.display = 'none';
}

// keep your original API names
window.openInstructionsPopup = () => open('instructionsPopup');
window.openDifficultyPopup  = () => open('difficultyPopup');
window.closeAllPopups       = closeAll;

document.addEventListener('DOMContentLoaded', () => {
  // Play goes to login (and hides any leftover popups)
  $('play-btn')?.addEventListener('click', (e) => {
    e.preventDefault();
    closeAll();
    window.location.href = '/login';
  });

  // click outside to close
  overlay?.addEventListener('click', closeAll);
});
