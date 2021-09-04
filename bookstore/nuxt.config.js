const path = require('path')
const fs = require('fs')
const env = process.env.NODE_ENV

const envPath = path.resolve(
  process.cwd(),
  env !== 'development' ? `.env.${env}` : '.env.dev'
)
const defaultEnvPath = path.resolve(process.cwd(), '.env')

require('dotenv').config({
  path: fs.existsSync(envPath) ? envPath : defaultEnvPath
})

console.info(`Using ${env} environment variables`)

export default {
  head: {
    title: 'Bookstore',
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

  css: [],

  plugins: [],

  components: true,

  buildModules: [
    '@nuxtjs/eslint-module'
  ],

  modules: [
    'bootstrap-vue/nuxt',
    '@nuxtjs/axios',
    '@nuxtjs/pwa'
  ],

  axios: {},

  pwa: {
    manifest: {
      lang: 'en'
    }
  },

  build: {
  }
}
