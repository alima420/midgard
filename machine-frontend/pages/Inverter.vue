<template>
    <div>
      <HeaderWithMenu />
      <div class="inverter">
        <h1>Inverter</h1>
        <div v-if="inverterData">
          <ul>
            <li v-for="(value, key) in formattedData" :key="key">
              <strong>{{ key }}:</strong> {{ value }}
            </li>
          </ul>
        </div>
        <div v-else>
          <p>Loading...</p>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import HeaderWithMenu from '../components/HeaderWithMenu.vue';
  import AWS from 'aws-sdk';
  
  export default {
    name: 'Inverter',
    components: {
      HeaderWithMenu,
    },
    data() {
      return {
        inverterData: null,
      };
    },
    computed: {
      formattedData() {
        if (!this.inverterData) return {};
  
        const data = this.inverterData.data;
        const keys = [
          'timestamp', 'w', 'runtime', 'whruntime', 'dca', 'dcv', 'fgrid', 
          'iline', 'tramp', 'vbias', 'vref', 'phvpha', 'spare1', 'spare2', 
          'trecl', 'tmpot', 'status'
        ];
  
        return keys.reduce((acc, key) => {
          if (data[key] && data[key].length > 0) {
            acc[key] = data[key][0];
          } else {
            acc[key] = 'N/A';
          }
          return acc;
        }, {});
      }
    },
    created() {
      this.fetchInverterData();
    },
    methods: {
      async fetchInverterData() {
        const url = 'https://fab.solarnative.cloud/v1/debug/inverter/data';
        const region = 'eu-central-1';
        const service = 'execute-api';
        const awsAccessKeyId = 'awsAccessKeyId';
        const awsSecretAccessKey = 'awsSecretAccessKey';
        const awsSessionToken = 'awsSessionToken';
        const credentials = new AWS.Credentials(awsAccessKeyId, awsSecretAccessKey, awsSessionToken);
        AWS.config.update({ region, credentials });
  
        const request = new AWS.HttpRequest(url, region);
        request.method = 'POST';
        request.headers['host'] = new URL(url).host;
        request.headers['Content-Type'] = 'application/json';
        request.body = JSON.stringify({
          meta: {
            pagination: {
              limit: 1
            }
          },
          identifierType: 'ProductSerial',
          identifierValue: '00000200002QC6'
        });
  
        const signer = new AWS.Signers.V4(request, service);
        signer.addAuthorization(credentials, new Date());
  
        try {
          const response = await this.$axios.$post(url, request.body, {
            headers: request.headers
          });
          this.inverterData = response;
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      }
    }
  };
  </script>
  
  <style>
  .inverter {
    margin: 10px;
    padding: 15px;
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
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
    position: relative;
    z-index: 1;
    height: 60px;
  }
  
  h1 {
    font-size: 1.5em;
    margin: 0;
    flex: 1;
  }
  
  .menu-toggle {
    font-size: 1.5em;
    background: none;
    border: none;
    color: #fff;
    cursor: pointer;
    margin-right: 10px;
  }
  
  ul {
    list-style-type: none;
    padding: 0;
    margin: 5px;
    padding: 15px;
    background: #ececec;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  
  }
  
  li {
    margin-bottom: 8px;
  }
  
  strong {
    display: inline-block;
    width: 120px;
    font-weight: bold;
  }
  </style>
  