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
          color="white"
          text
          @click="addItem(book) + $forceUpdate() + showAlert()"
        >
          <v-icon left>mdi-cart</v-icon> Add to cart
        </v-btn>
      </v-card-actions>
    </v-card>
    <v-alert type="success" :value="alert" class="mt-2">
      Added {{ book.name }} to cart
    </v-alert>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
export default {
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
      addItem: 'cart/addItem',
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
