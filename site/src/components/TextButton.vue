<template>
  <div>
    <input v-model="id" type="integer" placeholder="ID">
    <input v-model="text" type="text" placeholder="Text">
    <button @click="createMessage">Create message</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      id: null,
      text: null
    }
  },
  methods: {
    async createMessage() {
      const response = await fetch("http://127.0.0.1:8000/messages", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: this.id, text: this.text })
      });
      const data = await response.json();
      console.log(data);
    }
  }
}
</script>
