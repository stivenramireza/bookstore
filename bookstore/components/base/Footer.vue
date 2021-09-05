<template>
  <v-footer dark padless>
    <v-card
      flat
      tile
      class="blue-grey darken-4 white--text text-center card-container"
    >
      <v-card-text>
        <v-btn
          v-for="(item, index) in icons"
          :key="index"
          :href="item.link"
          target="_blank"
          icon
        >
          <v-icon size="35px">
            {{ item.name }}
          </v-icon>
        </v-btn>
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        © {{ $store.state.currentYear }} <strong>Bookstore</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
export default {
  data: () => ({
    icons: [
      {
        name: 'mdi-facebook',
        link: 'https://www.facebook.com/',
      },
      {
        name: 'mdi-instagram',
        link: 'https://www.instagram.com/',
      },
      {
        name: 'mdi-whatsapp',
        link: 'https://web.whatsapp.com/',
      },
    ],
  }),
}
</script>

<style scoped>
.card-container {
  width: 100%;
}
</style>
