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
        const awsAccessKeyId = 'ASIATFDF4VDRN64NV52B';
        const awsSecretAccessKey = '6GWsjSWyl9ZwzpjZ1Gwrj73eHE5mbtoFKm5glJ1i';
        const awsSessionToken = 'IQoJb3JpZ2luX2VjENr//////////wEaDGV1LWNlbnRyYWwtMSJIMEYCIQDF7a1Rq7v9mEqX9ekDA45g3LCGE5mfQk30AaoDPZAASAIhAMuYEoIkU1O7DzcuSvladmW2bVPkNeQwZRCZjx7olqSkKt8ECMP//////////wEQABoMMjE3MTA5NTM5MDQyIgwHfJY8t+s66XjL4K0qswSCjr+cd/wLU9Devk0t4D9ExCfSTPF6PerTWnMhgnBsAe0vHgoEolqg7e+NGU9avZKMDW2gyaaXwm9LSHi/3wVH3OVl0SHQKqS3QFmLnDxRPaBvE5obS0y+gei5CvjslY6T2IWPQLiOmNKoswik6nh79WpJxKlxlO39L0OoVN2o2PmvxWWsHPwQHVeFH/AF00H+rbI8hW4SbNVN1CrRbOPmEnOh89mZbaGaOEj/en7lOKAC8hj5jntQBx3gZq94qCJgbo5kko3EmEf3jwsF5w7l9As4qZNzrbTzhi34SdsjWJswraXWK5Z8Sh04I29JSd0mpZhkl8HX9Og0gHFNkLMAGyXTVAXJrM0VwbiX95izWmXgGyFkcWTJSrsZQ86z3VQQRu4gAXXso9/4wrG4TQmKEoUQgZp7XVlQkhREVgYRmZo7QzkDtbxS59Vq2pWh2WydWs5M5s5sunaeoDrw1Gpmt/UABj7JbCHDrc/9kPkgLZoWn1v+MRpEazXAIzHcIGIFvdmEQUc3qsUPMfZa15Q2cKetRVyxgYk0wG4ZIuGquTbgc/yhiXpYBN1+Vqx0bH9IGQpcUk08beYhs/YgT7MRLbODq2YlA08EPczLE4lcQ0IfuNgZZ73VpayOLzwxG++itb45VzOzThnbnEg/v8pHt9xE2UTNYduZfIH1bOEWzEIQZ0fkG3RbjglP+8aTbeGjogoLEr9epBWl593O9IgtbaoA/ivFx6GZyyctsMXatnORJjC4jL+1BjqEAjbwaQmQKdmaDHcLpvvKo60laE2osCtP38ZANM9eVMNn37NAXOklA7Vb9UoN1fTo1363rXjcEBN5ZwzGiqz/VhPk8ohwIwth58rK7KYmLZJixAX+Ub4mffnj98RZVb+pDo1FDnQjGbYCemlxKO8F9HsYCc/7+PU9C+CX2eDTC1j+0+NSe5RjP/1NXwxS5hL397T8f/R5hfp+7/3xLTyAoRBEDx/wGqiSYYlyw2Ch9NKmJTD0OEpgNCsHMfs5Oiwe/17XMj5hBZ9T/8oo+MqwWbFK5FHhdwcACxVJ6RlYyymJpeDRY2C/8ftREXlNuUsI3DRRjB5E31P9FTp003gS+fUJF1lg';
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
  