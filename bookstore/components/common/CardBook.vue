<template>
  <div>
    <v-card :id="book.book_id" color="blue-grey darken-4 white--text card-book">
      <v-img :src="book.image" height="400"></v-img>
      <v-card-title class="white--text">{{ book.name }}</v-card-title>
      <v-card-text class="white--text">Author: {{ book.author }}</v-card-text>
      <v-card-title class="white--text">{{
        book.price | priceFormat
      }}</v-card-title>
      <v-divider class="mx-4" color="white"></v-divider>
      <v-card-actions>
        <v-btn
          v-if="!book.selected"
          color="white"
          text
          @click="add(book) + $forceUpdate() + showAlert()"
        >
          <v-icon left>mdi-cart</v-icon> Add to cart
        </v-btn>
        <v-btn v-else @click="remove(book) + $forceUpdate() + showAlert()">
          <v-icon left>mdi-cart</v-icon> Remove from cart
        </v-btn>
        <v-btn color="white" text class="ml-auto">
          <v-icon left>mdi-plus</v-icon> See more
        </v-btn>
      </v-card-actions>
    </v-card>
    <v-alert v-if="book.selected" type="success" :value="alert" class="mt-2">
      Added {{ book.name }} to cart
    </v-alert>
    <v-alert v-else type="error" :value="alert" class="mt-2">
      Removed {{ book.name }} from cart
    </v-alert>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
const numeral = require('numeral')
export default {
  filters: {
    priceFormat: (value) => {
      return '$' + numeral(value).format('0,0,0,0,0')
    },
  },
  props: {
    book: {
      type: Object,
      default: () => {},
      required: true,
    },
  },
  data() {
    return {
      alert: false,
    }
  },
  methods: {
    ...mapMutations({
      add: 'cart/add',
      remove: 'cart/remove',
    }),
    showAlert() {
      this.alert = true
      setTimeout(() => {
        this.alert = false
      }, 2000)
    },
  },
}
</script>

<style scoped>
.card-book {
  width: 100%;
}
</style>
