function sendMessage() {
  const input = document.getElementById("userInput");
  const chatbox = document.getElementById("chatbox");
  const message = input.value.trim();
  if (!message) return;

  // Display user message
  chatbox.innerHTML += `<div><b>You:</b> ${message}</div>`;

  // Send message to backend using key "message" (to match app.py)
  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: message })  // fixed key name
  })
  .then(res => res.json())
  .then(data => {
    // Display bot response
    chatbox.innerHTML += `<div><b>Bot:</b> ${data.reply}</div>`;  // fixed to match backend JSON key
    chatbox.scrollTop = chatbox.scrollHeight;
  })
  .catch(err => {
    chatbox.innerHTML += `<div><b>Bot:</b> Error: ${err.message}</div>`;
  });

  input.value = "";
}

function startVoiceInput() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = "en-US";
  recognition.start();
  recognition.onresult = function(event) {
    document.getElementById("userInput").value = event.results[0][0].transcript;
    sendMessage();
  };
}
