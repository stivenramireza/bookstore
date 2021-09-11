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
      username: null,
    }
  },
  computed: {
    ...mapState({
      books: (state) => state.cart.books,
    }),
  },
  created() {
    this.username = this.$auth.user.username
  },
}
</script>
