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
          <td>{{ message[1] }}</td>
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
