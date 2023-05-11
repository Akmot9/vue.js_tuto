<template>
  <div>
    <input v-model="text" type="text" placeholder="Text">
    <button @click="createMessage">Create message</button>

    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Text</th>
          <th>Delete</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="message in messages" :key="message[0]">
          <td>{{ message[0] }}</td>
          <input type="text" v-model="message[1]" @input="onMessageInput(message[0], message[1])">
          <td>
            <input type="checkbox" :value="message[0]" v-model="selectedMessages">
          </td>
        </tr>
      </tbody>
    </table>
    <button @click="deleteMessages">Delete selected messages</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      text: null,
      messages: [],
      selectedMessages: []
    }
  },
  methods: {
    async createMessage() {
      const response = await fetch("http://127.0.0.1:8000/messages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: this.text })
      });
      const data = await response.json();
      console.log(data);
      this.getMessages(); // Reload messages after creating a new one
    },
    async getMessages() {
      const response = await fetch("http://127.0.0.1:8000/messages");
      const data = await response.json();
      this.messages = data.data;
    },
    async deleteMessages() {
      for (let messageId of this.selectedMessages) {
        const response = await fetch(`http://127.0.0.1:8000/messages?id=${messageId}`, {
          method: "DELETE",
          headers: { "Content-Type": "application/json" },
        });
        const data = await response.json();
        console.log(data);
      }
      this.selectedMessages = [];
      this.getMessages(); // Reload messages after deleting selected ones
    },
    async onMessageInput(id, text) {
    console.log(`Modification: ${text}`);
    // Envoyer les modifications à l'API ici, si nécessaire
    await fetch(`http://127.0.0.1:8000/messages/${id}`, {
          method: "PUT",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ id: id, text })
        });
  }
  },
  async mounted() {
    await this.getMessages(); // Get messages on initial load
    setInterval(async () => {
      await this.getMessages(); // Periodically get messages
    }, 10000); // Check every 10 seconds
  }
}
</script>

<style>
  table {
    border-collapse: collapse;
    margin-top: 20px;
    font-family: Arial, sans-serif;
    font-size: 14px;
  }
  th, td {
    border: 1px solid #35B6B4;
    text-align: left;
    padding: 8px;
  }
  th {
    background-color: #979394;
  }
  input[type="text"] {
    padding: 10px;
    font-size: 16px;
    border: 2px solid #2A96A8;
    border-radius: 5px;
    margin-right: 10px;
  }
  button {
    background-color: #66C1BF;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  button:hover {
    background-color: #092E3F;
  }
  .delete-button {
    background-color: #f44336;
  }
  .delete-button:hover {
    background-color: #d32f2f;
  }
  .checkbox {
    margin-right: 10px;
  }
</style>

