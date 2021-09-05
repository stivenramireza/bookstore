<template>
  <v-list color="blue-grey darken-3">
    <v-list-item>
      <v-list-item-avatar></v-list-item-avatar>
      <v-list-item-title class="product"
        ><strong>Book</strong></v-list-item-title
      >
      <v-list-item-title><strong>Quantity</strong></v-list-item-title>
      <v-list-item-title><strong>Price</strong></v-list-item-title>
    </v-list-item>
    <v-list-item v-for="(item, index) in books" :key="index" color="white">
      <v-list-item-avatar>
        <v-img :src="item.image"></v-img>
      </v-list-item-avatar>
      <v-list-item-title class="product"> {{ item.name }}</v-list-item-title>
      <v-list-item-title v-if="item.book_id">
        <v-select
          :value="item.quantity"
          background-color="blue-grey darken-3"
          :items="[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
          color="white"
          item-color="blue-grey darken-3"
          dark
          @change="updateCart({ quantity: $event, book_id: item.book_id })"
        >
        </v-select>
      </v-list-item-title>
      <v-list-item-title v-else>{{ item.quantity }}</v-list-item-title>
      <v-list-item-title>{{ item.price | priceFormat }}</v-list-item-title>
    </v-list-item>
    <v-list-item>
      <v-list-item-avatar color="white--text"
        ><strong>Total</strong></v-list-item-avatar
      >
      <v-list-item-title class="product"></v-list-item-title>
      <v-list-item-title></v-list-item-title>
      <v-list-item-title
        ><strong>{{ totalPrice | priceFormat }}</strong></v-list-item-title
      >
    </v-list-item>
  </v-list>
</template>

<script>
import { mapState, mapMutations, mapGetters } from 'vuex'
const numeral = require('numeral')
export default {
  filters: {
    priceFormat: (value) => {
      return '$' + numeral(value).format('0,0,0,0,0')
    },
  },
  computed: {
    ...mapState({
      books: (state) => state.cart.books,
    }),
    ...mapGetters({
      totalPrice: 'cart/totalPrice',
    }),
  },
  methods: {
    ...mapMutations({
      updateCart: 'cart/updateCart',
    }),
  },
}
</script>

<style scoped>
@media (min-width: 320px) and (max-width: 592px) {
  .product {
    display: none;
  }
}
</style>
