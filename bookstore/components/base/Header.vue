<template>
  <v-app-bar color="blue-grey darken-4" dense fixed clipped-left app>
    <v-toolbar-title
      class="mr-5 align-center toolbar-title pl-0"
      @click="$router.push('/')"
    >
      <span class="title white--text">Bookstore</span>
    </v-toolbar-title>
    <v-spacer />
    <v-toolbar-title class="ml-5 align-center">
      <span class="header-item toolbar-options" @click="$router.push('/about')"
        >About</span
      >
      <span v-if="books.length !== 0" class="header-item">
        <Cart :items="books" />
      </span>
      <v-btn v-if="!loggedIn" color="white" text @click="logout()"
        ><v-icon left>mdi-login</v-icon> Login</v-btn
      >
      <v-btn v-else color="white" text @click="logout()"
        ><v-icon left>mdi-logout</v-icon> Logout</v-btn
      >
    </v-toolbar-title>
  </v-app-bar>
</template>

<script>
import { mapState } from 'vuex'
import Cart from '@/components/common/Cart'

export default {
  components: {
    Cart,
  },
  data() {
    return {
      drawer: false,
      items: [
        {
          icon: 'mdi-television',
          text: 'Acerca de nosotros',
          link: '/nosotros',
        },
      ],
      loggedIn: false,
    }
  },
  computed: {
    ...mapState({
      books: (state) => state.cart.books,
    }),
  },
  created() {
    this.loggedIn = this.$auth.strategy.token.get()
  },
  methods: {
    login() {
      this.$auth.loginWith('awsCognito')
    },
    logout() {
      this.$auth.logout()
    },
  },
}
</script>

<style>
.header-item {
  color: white;
  font-size: 16px;
  margin-left: 20px;
}
.header-item:hover {
  font-weight: bold;
  cursor: pointer;
}
.navigation-icon:hover {
  cursor: pointer;
}
.toolbar-title:hover {
  cursor: pointer;
}
.v-list-item .v-list-item__title {
  color: white;
}
.v-list-item:hover {
  background: #546e7a;
}
.dot-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.dot {
  background: red;
  border-radius: 50%;
  height: 26px;
  width: 26px;
  line-height: 26px;
  display: inline-block;
  text-align: center;
  margin-right: 6px;
  font-weight: bold;
}
@media (min-width: 320px) and (max-width: 700px) {
  .toolbar-options {
    display: none;
  }
}
</style>
