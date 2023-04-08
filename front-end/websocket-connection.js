let socket = new WebSocket("ws://localhost:8000/ws/sc/calc/");

// send message from the form
document.forms.publish.onsubmit = function() {
  let outgoingMessage = this.message.value;

  socket.send(outgoingMessage);
  return false;
};

socket.onopen = function(e) {
  let messageElem = document.createElement('div');
  messageElem.textContent = "Websocket Connection Status : Connection established";
  document.getElementById('ws- connection-status').prepend(messageElem);
};

socket.onmessage = function(event) {
  let message = event.data;

  let result = document.createElement('div');
  result.textContent = message;
  document.getElementById('messages').prepend(result);
};

socket.onclose = function(event) {
  let status = document.createElement('div');
  status.textContent = "Websocket Connection Status : Disconnected";
  document.getElementById('ws- connection-status').prepend(status);
};

socket.onerror = function(error) {
  let status = document.createElement('div');
  status.textContent = "Websocket Connection Status : Fail to Connect";
  document.getElementById('ws- connection-status').prepend(status);
};