<template>
  <div class="edit-data">
    <h2>Edit Server Data</h2>
    <div class="info-container">
      <div class="info-item">
        <label for="status">Status:</label>
        <input id="status" type="text" v-model="machine.status" />
      </div>
      <div class="info-item">
        <label for="program">Program:</label>
        <input id="program" type="text" v-model="machine.program" />
      </div>
      <div class="info-item">
        <label for="counter">Counter:</label>
        <input id="counter" type="number" v-model="machine.counter" />
      </div>
    </div>
    <button @click="updateMachine">Update Machine</button>
  </div>
</template>

<script>
export default {
  props: {
    machine: Object,
  },
  methods: {
    updateMachine() {
      this.$emit('update-machine', this.machine);
    },
  },
};
</script>

<style scoped>
.edit-data {
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin: 10px;
    padding: 15px;
}

h2 {
    font-size: 1.25em;
    color: #007bff;
}

.info-container {
    display: flex;
    flex-direction: column;
    gap: 15px; /* Add some spacing between rows */
}

.info-item {
    display: flex;
    align-items: center;
    gap: 10px; /* Space between the label and input */
}

.info-item label {
    font-weight: bold;
    white-space: nowrap; /* Prevent the label from breaking */
}

input[type="text"],
input[type="number"] {
    width: 100%;
    padding: 8px;
    margin-top: 5px;
    border: 1px solid #ddd;
    border-radius: 4px;
    box-sizing: border-box;
}

button {
    background-color: #007bff;
    color: #fff;
    border: none;
    padding: 10px;
    border-radius: 4px;
    cursor: pointer;
    width: 100%;
    font-size: 1em;
    margin-top: 10px;
}

button:hover {
    background-color: #0056b3;
}

/* Media query for smaller screens */
@media (max-width: 600px) {
    .info-item {
        flex-direction: column;
        align-items: flex-start;
    }

    .info-item label {
        margin-bottom: 5px;
    }
}
</style>