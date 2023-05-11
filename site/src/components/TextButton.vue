<template>
  <div>
    <input v-model="text" type="text" placeholder="Text">
    <button @click="createMessage">Create message</button>

    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Text</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="message in messages" :key="message[0]">
          <td>{{ message[0] }}</td>
          <td>{{ message[1] }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      text: null,
      messages: []
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
    },
    async getMessages() {
      const response = await fetch("http://127.0.0.1:8000/messages");
      const data = await response.json();
      this.messages = data.data;
    }
  },
  async mounted() {
    await this.getMessages(); // Get messages on initial load
    setInterval(async () => {
      await this.getMessages(); // Periodically get messages
    }, 100000); // Check every 10 seconds
  }
}
</script>
