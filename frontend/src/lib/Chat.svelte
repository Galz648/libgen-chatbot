<script>
  export let messages = [];

  let inputText = "";

  function sendMessage(event) {
    event.preventDefault();
    const text = inputText.trim();
    if (text) {
      messages = [...messages, { text, sender: "user" }];
      inputText = "";
      receiveMessage();
    }
  }

  function receiveMessage() {
    messages = [...messages, { text: "Hi there!", sender: "bot" }];
  }
</script>


<div>
  {#each messages as message}
    <div class="message {message.sender}">
      <span>{message.sender}:{message.text}</span>
    </div>
  {/each}
</div>

<form on:submit={sendMessage}>
  <input type="text" placeholder="Type a message..." bind:value={inputText} />
  <button type="submit">Send / Receive message</button>
</form>
