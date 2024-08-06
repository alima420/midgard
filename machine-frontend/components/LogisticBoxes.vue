<template>
  <div class="logistic-boxes">
    <div class="tabs">
      <button
        class="tab-button"
        :class="{ active: activeTab === 'tab1' }"
        @click="showTab('tab1')"
      >
        Check boxes
      </button>
      <button
        class="tab-button"
        :class="{ active: activeTab === 'tab2' }"
        @click="showTab('tab2')"
      >
        View boxes
      </button>
      <button
        class="tab-button"
        :class="{ active: activeTab === 'tab3' }"
        @click="showTab('tab3')"
      >
        View products
      </button>
    </div>
    <div class="content1">
      <div class="input-section1" v-if="activeTab === 'tab1'">
        <div v-if="!data.length" class="input-title">
          <h3>Please scan a logistics box</h3>
        </div>
        <div v-if="!data.length" class="input-section">
          <input
            v-model="inputValue"
            @keyup.enter="fetchData"
            type="text"
            placeholder="Enter logistics box"
          />
          <button @click="fetchData">Apply</button>
        </div>
        <div v-if="loading" class="loading">Loading...</div>
        <div v-if="showSnackbar" class="snackbar">{{ error }}</div>
        <div v-if="data.length">
          <div class="input-title">
            <h3>Find and eliminate all the bad products!</h3>
            <button class="back-button" @click="resetData">Back</button>
          </div>
          <ul>
            <li
              v-for="item in data"
              :key="item.serial_number"
              :style="{ backgroundColor: item.flag ? '#d4edda' : (item.matched ? '#d4edda' : '#f8d7da') }"
              ><div class="serial-number-label">
                <div class ="serial-number-label1">{{ item.serial_number }}</div>
                <div class ="serial-number-label2">{{ item.details }}</div>
              </div>
            </li>
          </ul>
          <div class="input-section">
            <input
              v-model="searchValue"
              type="text"
              placeholder="Enter serial number"
              @keyup.enter="checkOffItem"
            />
            <button @click="checkOffItem">Check Off</button>
          </div>
        </div>
      </div>
      <div v-if="activeTab === 'tab2'">
        <div class="tab2-content">
          <div class="input-title2">
            <h3>View all logistics boxes</h3>
            <div class="input-section">
              <input 
              v-model="searchBoxId" 
              type="text" 
              placeholder="Search for logistics box number" 
              />
              <button @click="searchBox">Apply</button>
            </div>
          </div>
        </div>
        <div class="container">
          <div v-if="loading" class="loading">Loading...</div>
          <div v-if="error" class="error">{{ error }}</div>
          <div v-if="boxes.length === 0" class="no-results">No boxes found</div>
          <div class="box" v-for="box in boxes" :key="box.logistics_box_id"
            :style="{ backgroundColor: box.flag ? '#d4edda' : '#f8d7da' }">
            <div class="box-header">
              <strong>{{ box.logistics_box_id }}</strong>
            </div>
            <div class="box-details">
              <div>{{ box.details }}</div>
              <div>{{ box.exceptions.length }}</div>
            </div>
          </div>  
        </div>
      </div>
      <div v-if="activeTab === 'tab3'">
        <p>Content for Tab 3</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeTab: 'tab1',
      inputValue: '',
      searchValue: '',
      data: [],
      loading: false,
      error: null,
      logisticsBoxRegex: /^LB\d{2}(\d{4})$/,
      serialNumberRegex: /000002000[A-Z0-9]{5}/,
      showSnackbar: false,
      snackbarTimeout: null,
      boxes: [],
      searchBoxId: '',

    };
  },
  methods: {
    showTab(tab) {
      this.activeTab = tab;
    },
    async fetchData() {
      const match = this.logisticsBoxRegex.exec(this.inputValue);
      if (!match) {
        this.error = 'Invalid logistics box format';
        this.showSnackbar = true;
        clearTimeout(this.snackbarTimeout);
        this.snackbarTimeout = setTimeout(() => {
          this.showSnackbar = false;
        }, 3000);
        return;
      }

      const logisticsBoxId = match[1];
      this.loading = true;
      this.error = null;

      try {
        const response = await fetch(`http://127.0.0.1:8000/api/logisticsboxes/${logisticsBoxId}/exceptions/`);
        if (!response.ok) throw new Error('Network response was not ok');
        const result = await response.json();
        this.data = result.map(item => ({
          serial_number: item.serial_number,
          details: item.details,
          flag: item.flag,
          matched: item.flag,
          logistics_box: logisticsBoxId 
        }));
        this.$emit('box-scanned', logisticsBoxId);
        this.inputValue = '';
      } catch (err) {
        this.inputValue = '';
        this.error = err.message;
        this.data = [];
      } finally {
        this.loading = false;
      }
    },
    async checkOffItem() {
      const match = this.serialNumberRegex.exec(this.searchValue);
      if (!match) {
        this.error = 'Invalid serial number format';
        this.showSnackbar = true;
        this.searchValue = '';
        clearTimeout(this.snackbarTimeout);
        this.snackbarTimeout = setTimeout(() => {
          this.showSnackbar = false;
        }, 3000);
        return;
      }

      const serialNumber = match[0];
      this.error = null;

      const item = this.data.find(item => item.serial_number === serialNumber);
      if (item) {
        if (item.flag) {
          this.error = 'Serial number already checked off';
          this.showSnackbar = true;
          clearTimeout(this.snackbarTimeout);
          this.snackbarTimeout = setTimeout(() => {
            this.showSnackbar = false;
          }, 3000);
          this.searchValue = '';
          return;
        }

        item.matched = true;
        this.searchValue = '';

        try {
          const response = await fetch(`http://127.0.0.1:8000/api/exceptions/${item.serial_number}/`, {
            method: 'PATCH',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ flag: true }),
          });
          if (!response.ok) throw new Error('Failed to update flag');
          item.flag = true;
        } catch (err) {
          console.error(err);
        }
        this.$emit('product-scanned', item.serial_number);

        // Check if all items are flagged and update logistics box if so
        if (this.data.every(item => item.flag)) {
          const logisticsBoxId = item.logistics_box;
          try {
            await fetch(`http://127.0.0.1:8000/api/logisticsboxes/${logisticsBoxId}/`, {
              method: 'PATCH',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify({ flag: true }),
            });
            this.$emit('box-updated', logisticsBoxId); // Emit event when the logistics box is updated
          } catch (err) {
            console.error('Failed to update logistics box flag', err);
          }
        }
      } else {
        alert('Serial number not found');
      }
    },
    async fetchBoxes(url) {
      this.loading = true;
      this.error = null;

      try {
        const response = await fetch(url);
        if (!response.ok) throw new Error('Network response was not ok');
        const result = await response.json();
        this.boxes = result;
      } catch (err) {
        this.error = err.message;
        this.boxes = [];
      } finally {
        this.loading = false;
      }
    },
    searchBox() {
      const boxId = this.searchBoxId.trim();
      if (boxId) {
        this.fetchBoxes(`http://127.0.0.1:8000/api/logisticsboxes/${boxId}`);
      } else {
        this.fetchBoxes('http://127.0.0.1:8000/api/logisticsboxes/');
      }
    },
    resetData() {
      this.data = [];
      this.searchValue = '';
      this.$emit('reset-box');
    },
    created() {
    this.fetchBoxes('http://127.0.0.1:8000/api/logisticsboxes/');
    },
  },
};
</script>

<style scoped>
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

.logistic-boxes {
  background: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  margin: 10px;
  padding: 15px;
}

.tabs {
  display: flex;
  border-bottom: 2px solid #ddd; /* Underline for the tab bar */
  flex: 1;
}

.tab-button {
  flex: 1;
  padding: 10px;
  font-size: 14px;
  cursor: pointer;
  border: none;
  background: #f1f1f1; /* Light gray background for inactive tabs */
  color: #333;
  border-radius: 4px 4px 0 0; /* Rounded top corners */
  text-align: center; /* Center text horizontally */
  display: flex; /* Add flex display */
  justify-content: center; /* Center text horizontally */
  align-items: center; /* Center text vertically */
  transition: background-color 0.3s, border-bottom 0.3s;
  border-bottom: 2px solid #ddd;
}
.tab-button:hover {
  background-color: #e0e0e0; /* Slightly darker gray on hover */
}

.tab-button.active {
  background: #ffffff; /* White background for active tab */
  color: #000;
  border-bottom: 2px solid #007bff; /* Blue underline for the active tab */
  font-weight: bold;
}

.input-section {
  gap: 10px;
  width: 100%;
  margin-bottom: 15px;
  display: flex;
  padding-top: 5px;
}

.input-title {
  position: relative;
  display: flex;
  flex: 1;
  width: 100%;
  justify-content: space-between;
  align-items: center;
}


input[type="text"],
input[type="number"] {
  flex: 1 1 47%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
  box-sizing: border-box;
}

h3 {
  margin: 15px;
  margin-left: 3px;
}

button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1em;
}

.back-button {
  height: 35px;
  width: 50px;
  margin: 5px;
  padding: 5px;
}


.loading {
  color: #007bff;
  font-weight: bold;
}

.error {
  color: #ff0000;
  font-weight: bold;
}

.error-message {
  color: #ff0000;
  font-weight: bold;
  margin-top: 5px;
}

ul {
  list-style-type: none;
  padding: 0;
  align-items: center;
  margin: 0;
  margin-bottom: 15px;
  overflow-y: auto;
  max-height: 500px;
}

li {
  background: #fff;
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.snackbar {
  font-family: sans-serif;
  visibility: visible;
  min-width: 250px;
  margin-left: -125px;
  background-color: #333;
  color: #fff;
  text-align: center;
  border-radius: 2px;
  position: fixed;
  z-index: 1;
  bottom: 30px;
  left: 50%;
  font-size: 17px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  padding: 13px;
  border-radius: 3px;
}

/* .box {
  background-color: #007bff;
  color: #fff;
  border-radius: 8px;
  padding: 20px;
  max-height: 80px;
  flex: 1 1 15%;
  margin: 1%;
  margin-bottom: 1%;
  max-width: 500px;
  min-width: 100px;
} */

.container {
  display: flex;
  flex-wrap: wrap;
  overflow-y: auto;
  max-height: 500px;

}

.input-title2 {
  display: block;
  margin-bottom: 5px;
}

.search-section {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.search-section input {
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-right: 10px;
  flex: 1;
}

.search-section button {
  background-color: #007bff;
  color: #fff;
  border: none;
  padding: 10px;
  border-radius: 4px;
  cursor: pointer;
}

.search-section button:hover {
  background-color: #0056b3;
}

.boxes-container {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  
}

.box {
  flex: 1 1 calc(50% - 20px); /* 2 boxes per row */
  background: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 15px;
  box-sizing: border-box;
  flex-direction: column;
  margin: 3px;
  min-width: 100px;
}

.box-header {
  font-size: 16px;
  margin-bottom: 10px;
}

.box-details {
  display: flex;
  justify-content: space-between;
}

.loading {
  color: #007bff;
  font-weight: bold;
}

.error {
  color: #ff0000;
  font-weight: bold;
  text-align: center;
}

.no-results {
  text-align: center;
  font-weight: bold;
}

.serial-number-label {
  font-weight: bold;
  display: flex;
  justify-content: space-between;
}


</style>