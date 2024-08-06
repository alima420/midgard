<template>
  <div class="logistic-main" :class="{ 'flag-true': logisticsInfo && logisticsInfo.flag, 'flag-false': logisticsInfo && !logisticsInfo.flag }">
    <div class="info-container">
      <div v-if="logisticsInfo" class="logistics-info">
        <h3>Logistics Box ID: {{ logisticsInfo.logistics_box_id }}</h3>
        <p><strong>Details:</strong> {{ logisticsInfo.details }}</p>
        <p><strong>Flag:</strong> {{ logisticsInfo.flag }}</p>
        <p>{{ instructionalText }}</p>
      </div>
      <div v-else>
        <p>No logistics box selected. Please scan a logistics box.</p>
      </div>
    </div>
    <div class="button-container">
      <button @click="refreshComponent" class="refresh-button">Refresh</button>
      <button @click="setFlag(true)" class="flag-button flag-true-button">Set Flag True</button>
      <button @click="setFlag(false)" class="flag-button flag-false-button">Set Flag False</button>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    boxId: {
      type: String,
      default: null
    }
  },
  data() {
    return {
      logisticsInfo: null
    };
  },
  computed: {
    instructionalText() {
      if (this.logisticsInfo) {
        const details = this.logisticsInfo.details;
        if (/Januar|Februar/.test(details)) {
          return 'Instructional text 123';
        } else if (/März|April/.test(details)) {
          return 'Instructional text 456';
        }
      }
      return '';
    }
  },
  watch: {
    boxId: {
      immediate: true,
      handler(newBoxId) {
        if (newBoxId) {
          this.fetchLogisticsInfo(newBoxId);
        } else {
          this.logisticsInfo = null; // Clear logistics info when boxId is null
        }
      }
    }
  },
  methods: {
    async fetchLogisticsInfo(boxId) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/logisticsboxes/${boxId}`);
        if (!response.ok) throw new Error('Failed to fetch logistics box info');
        this.logisticsInfo = await response.json();
      } catch (error) {
        console.error(error);
        this.logisticsInfo = null;
      }
    },
    async setFlag(flagValue) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/logisticsboxes/${this.boxId}/`, {
          method: 'PATCH',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({ flag: flagValue }),
        });
        if (!response.ok) throw new Error('Failed to update flag');
        this.fetchLogisticsInfo(this.boxId); // Refresh data after updating flag
      } catch (error) {
        console.error('Failed to update logistics box flag', error);
      }
    },
    refreshComponent() {
      this.fetchLogisticsInfo(this.boxId); // Re-fetch the logistics info
    }
  }
};
</script>

<style scoped>
.logistic-main {
  display: flex;
  background: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: 10px;
  padding: 15px;
  justify-content: space-between;
}

.flag-true {
  background: #d4edda;
}

.flag-false {
  background: #f8d7da;
}

.info-container {
  flex: 1;
  margin-right: 10px;
}

.button-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

button {
  width: 120px;
  margin-bottom: 10px;
  padding: 10px;
  border: none;
  cursor: pointer;
  border-radius: 5px;
}

.refresh-button {
  background-color: yellow;
  color: black;
}

.flag-true-button {
  background-color: green;
  color: white;
}

.flag-false-button {
  background-color: red;
  color: white;
}
</style>
