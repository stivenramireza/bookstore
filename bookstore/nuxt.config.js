export default {
  ssr: false,
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

  plugins: [{ src: '~/plugins/filters', ssr: false }, { src: '~/plugins/vuex-persist', ssr: false }],

  components: true,

  buildModules: ['@nuxtjs/eslint-module'],

  modules: ['@nuxtjs/axios', '@nuxtjs/pwa', '@nuxtjs/vuetify', '@nuxtjs/auth-next'],

  auth: {
    strategies: {
      awsCognito: {
        scheme: 'oauth2',
        endpoints: {
          authorization: `${process.env.AWS_COGNITO_DOMAIN}/login`,
          token: `${process.env.AWS_COGNITO_DOMAIN}/oauth2/token`,
          userInfo: `${process.env.AWS_COGNITO_DOMAIN}/oauth2/userInfo`,
          logout: `${process.env.AWS_COGNITO_DOMAIN}/logout`
        },
        token: {
          property: 'access_token',
          type: 'Bearer',
          maxAge: 3600
        },
        refreshToken: {
          property: 'refresh_token',
          maxAge: 60 * 60 * 24 * 30
        },
        responseType: 'token',
        redirectUri: `${process.env.BOOKSTORE_DOMAIN}/login`,
        logoutRedirectUri: `${process.env.BOOKSTORE_DOMAIN}/login`,
        clientId: process.env.AWS_COGNITO_CLIENT_ID,
        scope: ['email', 'openid', 'profile'],
        codeChallengeMethod: 'S256'
      }
    }
  },

  axios: {},

  env: {
    BOOKSTORE_DOMAIN: process.env.BOOKSTORE_DOMAIN,
    AWS_COGNITO_DOMAIN: process.env.AWS_COGNITO_DOMAIN,
    AWS_COGNITO_CLIENT_ID: process.env.AWS_COGNITO_CLIENT_ID,
    BOOKS_API: process.env.BOOKS_API,
    ORDERS_API: process.env.ORDERS_API
  },

  pwa: {
    manifest: {
      lang: 'en'
    }
  },

  build: {
    extend(config, ctx) {
      if (ctx.isDev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue|ts)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/,
          options: {
            fix: true,
          },
        })
      }
    }
  }
}
