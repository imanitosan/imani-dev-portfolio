// script.js
const text = "Imani";  // Change this to your name or desired text
const typingElement = document.getElementById("typing-effect");
let index = 0;

function typeWriter() {
  if (index < text.length) {
    typingElement.innerHTML += text.charAt(index);
    index++;
    setTimeout(typeWriter, 200);  // Adjust typing speed here (ms)
  }
}

// Start typing effect when the page loads
window.onload = typeWriter;
