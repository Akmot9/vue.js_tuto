<template>
    <div>
      <textarea v-model="text" placeholder="Enter your text here"></textarea>
      <button @click="onClick">Submit</button>
      <p v-if="submitted">You entered: {{ text }}</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        text: "",
        submitted: false
      };
    },
    methods: {
      onClick() {
        // Handle button click event
        this.submitted = true;
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
  