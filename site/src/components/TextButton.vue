<template>
    <div>
      <textarea v-model="text" placeholder="Enter your text here"></textarea>
      <button @click="onClick">Submit</button>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        text: ""
      };
    },
    methods: {
      onClick() {
        // Handle button click event
        console.log("Button clicked!");
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
  