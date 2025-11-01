// welcomepageJava.js (compact)
const $ = (id) => document.getElementById(id);
const overlay = $('overlay');
const POPUPS = ['instructionsPopup'];

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
window.goToLogin = () => window.location.href = '/login';
window.closeAllPopups = closeAll;

document.addEventListener('DOMContentLoaded', () => {
  // click outside to close
  overlay?.addEventListener('click', closeAll);
});
