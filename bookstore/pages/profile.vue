<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card>
        <v-card-title class="headline">
          Welcome {{ username }}, you are logged in!
        </v-card-title>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
import { mapState } from 'vuex'

export default {
  middleware: 'auth',
  data() {
    return {
      email: null,
      phoneNumber: null,
      userId: null,
      username: null,
      accessToken: null,
      refreshToken: null,
    }
  },
  computed: {
    ...mapState({
      books: (state) => state.cart.books,
    }),
  },
  created() {
    console.log(this.books)
    this.email = this.$auth.user.email
    this.phoneNumber = this.$auth.user.phone_number
    this.userId = this.$auth.user.sub
    this.username = this.$auth.user.username
    this.accessToken = this.$auth.strategy.token.get()
    this.refreshToken = this.$auth.strategy.refreshToken.get()
  },
  methods: {
    logOut() {
      this.$auth.logout()
    },
  },
}
</script>
