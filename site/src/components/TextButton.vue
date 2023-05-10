<template>
    <div>
      <textarea v-model="text" placeholder="Enter your text here"></textarea>
      <button @click="onClick">Submit</button>
      <p v-if="submitted">You entered: {{ text }}</p>
    </div>
  </template>
  
  <script>
  import axios from "axios";

  export default {
    data() {
      return {
        text: "",
        submitted: false
      };
    },
    methods: {
        onClick() {
            // Send message using Axios
            axios.post("http://localhost:8000/messages", { text: this.text })
            .then(response => {
            console.log("Message sent:", response.data);
            this.submitted = true;
        })
        .catch(error => {
        console.error("Error sending message:", error);
    });
}
    }
  };
  </script>
  
  <style scoped>
  textarea {
    width: 100%;
    height: 100px;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
  }
  button {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
  }
  </style>
  