<template>
  <div>
    <HeaderWithMenu />
    <!-- Display Server Data -->
    <ServerData v-if="serverData" :serverData="serverData" @refresh="refreshData" />

    <!-- Form to Update Machine Data -->
    <EditData v-if="machine" :machine="machine" @update-machine="handleUpdateMachine" />
  </div>
</template>

<script>
import ServerData from '~/components/ServerData.vue';
import EditData from '~/components/EditData.vue';
import HeaderWithMenu from '~/components/HeaderWithMenu.vue';

export default {
  components: {
    ServerData,
    EditData,
    HeaderWithMenu,
  },
  data() {
    return {
      machine: null,
      serverData: null,
      socket: null,
    };
  },
  async mounted() {
    await this.fetchMachineData();
    this.initWebSocket();
  },
  beforeDestroy() {
    if (this.socket) {
      this.socket.close();
    }
  },
  methods: {
    async fetchMachineData() {
      try {
        const response = await this.$axios.get('http://127.0.0.1:8000/api/update/M2/');
        this.machine = { ...response.data };
        this.serverData = response.data;
      } catch (error) {
        console.error('Failed to fetch machine data:', error);
      }
    },
    async refreshData() {
      await this.fetchMachineData();
    },
    async handleUpdateMachine(updatedMachine) {
      try {
        // Send updated machine data to the server
        if (this.socket) {
          this.socket.send(JSON.stringify(updatedMachine));
        }
        // Refresh server data after update
        await this.refreshData();
      } catch (error) {
        console.error('Failed to update machine data:', error);
      }
    },
    initWebSocket() {
      const socket = new WebSocket('ws://127.0.0.1:8000/ws/machine/M2/');
      socket.onopen = () => {
        console.log('WebSocket connected');
      };
      socket.onmessage = (event) => {
        this.serverData = JSON.parse(event.data);
      };
      socket.onerror = (error) => {
        console.error('WebSocket error:', error);
      };
      socket.onclose = () => {
        console.log('WebSocket closed');
      };
      this.socket = socket;
    }
  }
};
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f0f0f0;
}

header {
  display: flex;
  align-items: center;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  position: relative; /* Make the header relative to position elements inside it */
  z-index: 1; /* Ensure the header is above other content */
  height: 60px;
}

h1 {
  font-size: 1.5em;
  margin: 0;
  flex: 1; /* Allow the header title to take up the remaining space */
}

.menu-toggle {
  font-size: 1.5em;
  background: none;
  border: none;
  color: #fff;
  cursor: pointer;
  margin-right: 10px; /* Space between the icon and title */
}
</style>