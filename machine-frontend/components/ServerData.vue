<template>
  <div class="logistic-boxes">
    <div class="header">
      <h2>{{ formattedName }}</h2>
      <button class="refresh-button" @click="handleRefresh">Refresh</button>
    </div>
    <div class="info-container">
      <p><strong>Status:</strong> {{ serverData.status }}</p>
      <p><strong>Program:</strong> {{ serverData.program }}</p>
      <p><strong>Counter:</strong> {{ serverData.counter }}</p>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    serverData: Object,
  },
  computed: {
    formattedName() {
      let ipAddress = '';
      switch (this.serverData.name) {
        case 'M1':
          ipAddress = '192.168.1.151';
          break;
        case 'M2':
          ipAddress = '192.168.1.161';
          break;
        case 'M3':
          ipAddress = '192.168.1.171';
          break;
        default:
          ipAddress = 'Unknown IP';
      }
      return `${this.serverData.name} - ${ipAddress}`;
    }
  },
  methods: {
    handleRefresh() {
      this.$emit('refresh');
    }
  }
}
</script>
  
<style scoped>
.logistic-boxes {
  background: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: 10px;
  padding: 15px;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center; /* Vertically center the items */
  margin-bottom: 20px;
}

.refresh-button {
  padding: 5px 10px;
  font-size: 14px;
  cursor: pointer;
  border: 1px solid #000;
  background-color: #ffd900;
  color: rgba(0, 0, 0);
  border-radius: 4px;
  width: auto; /* Ensures the width is based on content */
  max-width: 100px; /* Limits the maximum width */
  text-align: center; /* Centers the text inside the button */
}

.refresh-button:hover {
  background-color: #ecc900;
  color: rgba(0, 0, 0);
}

.info-container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px; /* Space between items */
}

.info-container p {
  margin: 0;
  flex: 1;
}

</style>
