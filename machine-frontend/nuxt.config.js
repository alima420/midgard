export default {
  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'machine-frontend',
    htmlAttrs: {
      lang: 'en'
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [
    'material-symbols',
  ],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    // '~/plugins/websocket.client.js',
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/proxy',
  ],

  axios: {
    baseURL: 'http://192.168.1.121:8000/api/',
    proxy: true,
  },

  // proxy: {
  //   '/api/': {
  //     target: 'https://fab.solarnative.cloud',
  //     pathRewrite: {'^/api/': ''},
  //     changeOrigin: true,
  //   },
  // },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
  },

  features: {
    inlineStyles: false,  
  },

  server: {
    host: '192.168.1.121',
    port: '3000' // optional
},
}
