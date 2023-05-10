<template>
    <div>
      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Text</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="message in messages" :key="message.id">
            <td>{{ message.id }}</td>
            <td>{{ message.text }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      messages: {
        type: Array,
        required: true
      }
    }
  }
  </script>
  