<template>
  <v-row justify="center" align="center">
    <v-col cols="12" sm="8" md="6">
      <v-card>
        <v-card-title class="headline">
          Welcome {{ username }}, you are logged in!
        </v-card-title>
        <v-card-text>
          <p>
            Here are your user details, retrieved from the
            <a
              href="https://docs.aws.amazon.com/cognito/latest/developerguide/userinfo-endpoint.html"
              >/USERINFO</a
            >
            endpoint:
          </p>
          <template>
            <v-simple-table>
              <template #default>
                <thead>
                  <tr>
                    <th class="text-left">Property</th>
                    <th class="text-left">Value</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td>Email</td>
                    <td>{{ email }}</td>
                  </tr>
                  <tr>
                    <td>Phone number</td>
                    <td>{{ phoneNumber }}</td>
                  </tr>
                  <tr>
                    <td>UserId/sub</td>
                    <td>{{ userId }}</td>
                  </tr>
                  <tr>
                    <td>User name</td>
                    <td>{{ username }}</td>
                  </tr>
                  <tr>
                    <td>Access Token</td>
                    <td>{{ accessToken }}</td>
                  </tr>
                  <tr>
                    <td>Refresh Token</td>
                    <td>{{ refreshToken }}</td>
                  </tr>
                </tbody>
              </template>
            </v-simple-table>
          </template>
        </v-card-text>
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
