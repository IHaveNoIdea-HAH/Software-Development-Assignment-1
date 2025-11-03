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

  // Create falling images
  const container = $('fallingContainer');
  if (!container) return;

  // List of image files in your imagesHomepage folder
  const imageFiles = ['image1.png', 'image2.png', 'image3.png', 'image4.png','image5.png','image6.png','image7.png','image8.png','image9.png','image10.png']; // Add more image filenames as needed
  const fallingDuration = 8; // Duration in seconds for images to fall
  const spawnRate = 300; // Milliseconds between spawning new images

  function createFallingImage() {
    const img = document.createElement('img');
    let randomImage;
    if (Math.random() < 0.005) {
      randomImage = 'image11.png';
    } else {
      randomImage = imageFiles[Math.floor(Math.random() * imageFiles.length)];
    }
    img.src = `http://localhost:5000/static/imagesHomepage/${randomImage}`;
    img.className = 'falling-image';
    
    const randomLeft = Math.random() * (window.innerWidth - 50);
    img.style.left = randomLeft + 'px';
    img.style.animationDuration = fallingDuration + 's';
    
    container.appendChild(img);

    // Remove image after animation completes
    setTimeout(() => img.remove(), fallingDuration * 1000 + 2000);
  }

  // Spawn falling images at intervals
  setInterval(createFallingImage, spawnRate);
});