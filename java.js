const modeToggle = document.getElementById('mode-toggle');
const body = document.body;

modeToggle.addEventListener('click', function() {
  body.classList.toggle('dark-mode');
  // Toggle between moon and sun icon
  if (modeToggle.textContent === '🌙') {
    modeToggle.textContent = '☀️'; // Change icon to sun
  } else {
    modeToggle.textContent = '🌙'; // Change icon to moon
  }
});