<template>
  <div class="container">
    <HeaderWithMenu />
    <LogisticBoxes 
      @box-scanned="handleBoxScanned" 
      @reset-box="handleResetBox" 
      @product-scanned="handleProductScanned"
      @box-updated="handleBoxUpdated" />
    <LogisticsInfo :boxId="scannedBoxId" :key="scannedBoxId" />
    <ProductInfo :serialNumber="scannedProductSerial" />
  </div>
</template>

<script>
import HeaderWithMenu from '~/components/HeaderWithMenu.vue';
import LogisticBoxes from '../components/LogisticBoxes.vue';
import LogisticsInfo from '../components/LogisticsInfo.vue';
import ProductInfo from '../components/ProductInfo.vue';

export default {
  components: {
    HeaderWithMenu,
    LogisticBoxes,
    LogisticsInfo,
    ProductInfo,
  },
  data() {
    return {
      scannedBoxId: null,
      scannedProductSerial: null,
    };
  },
  methods: {
    handleBoxScanned(boxId) {
      this.scannedBoxId = boxId;
    },
    handleResetBox() {
      this.scannedBoxId = null;
      this.scannedProductSerial = null; // Clear product info when box is reset
    },
    handleProductScanned(serialNumber) {
      this.scannedProductSerial = serialNumber;
    },
    handleBoxUpdated(boxId) {
      this.scannedBoxId = null; // Force re-render of LogisticsInfo component
      this.$nextTick(() => {
        this.scannedBoxId = boxId; // Set the boxId again to refresh the component
      });
    }
  },
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

