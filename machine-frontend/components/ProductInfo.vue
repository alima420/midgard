<template>
    <div class="product-info" v-if="productInfo">
      <h3>Product Serial: {{ productInfo.product_serial }}</h3>
      <p><strong>Logistics Box ID:</strong> {{ productInfo.logistics_box_id }}</p>
      <p><strong>Logistics Box Timestamp:</strong> {{ productInfo.logistics_box_timestamp }}</p>
      <p><strong>Number of Units:</strong> {{ productInfo.number_units }}</p>
      <p><strong>Article Number:</strong> {{ productInfo.article_number }}</p>
      <p><strong>Device Creation Timestamp:</strong> {{ productInfo.device_creation_timestamp }}</p>
      <p><strong>Device Remarks:</strong> {{ productInfo.device_remarks }}</p>
    </div>
    <div v-else>
      <p class="else">No product box information available. Please scan a product box.</p>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      serialNumber: {
        type: String,
        default: null,
      },
    },
    data() {
      return {
        productInfo: null,
      };
    },
    watch: {
      serialNumber: {
        immediate: true,
        handler(newSerialNumber) {
          if (newSerialNumber) {
            this.fetchProductInfo(newSerialNumber);
          } else {
            this.productInfo = null; // Clear product info when serial number is null
          }
        },
      },
    },
    methods: {
      async fetchProductInfo(serialNumber) {
        try {
          const response = await fetch(`http://127.0.0.1:8000/api/productboxes/${serialNumber}/`);
          if (!response.ok) throw new Error('Failed to fetch product box info');
          this.productInfo = await response.json();
        } catch (error) {
          console.error(error);
          this.productInfo = null;
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .product-info {
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin: 10px;
    padding: 15px;
  }

  .else{
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin: 10px;
    padding: 15px;
  }

  </style>
  