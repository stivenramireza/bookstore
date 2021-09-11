<template>
  <div class="text-center">
    <p v-if="orderStatus == null" class="order-section">
      Processing your order...
    </p>
    <div v-if="orderStatus == 'success'">
      <p class="order-section">Your order has been confirmed successfully.</p>
      <img
        src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/13/Facebook_like_thumb.png/1196px-Facebook_like_thumb.png"
        alt="success-confirm"
        height="300"
        width="300"
      />
      <v-row class="mt-4 btn-orders">
        <v-btn
          tile
          color="blue-grey darken-4 white--text"
          @click="$router.push('/orders')"
        >
          See your orders
        </v-btn>
      </v-row>
    </div>
    <div v-if="orderStatus == 'error'">
      <p class="order-section">Error to confirm your order. Try again!</p>
      <img
        src="http://theblockheadswiki.com/images/thumb/c/cb/Warning.png/900px-Warning.png"
        alt="error-confirm"
        height="300"
        width="300"
      />
    </div>
  </div>
</template>

<script>
import { mapState, mapGetters, mapMutations } from 'vuex'

export default {
  middleware: 'auth',
  data() {
    return {
      orderStatus: null,
    }
  },
  computed: {
    ...mapState({
      books: (state) => state.cart.books,
    }),
    ...mapGetters({
      totalPrice: 'cart/totalPrice',
    }),
  },
  async mounted() {
    try {
      const url = `${process.env.ORDERS_API}/order`
      await this.$axios.$post(url, {
        customer: {
          username: this.$auth.user.username,
          email: this.$auth.user.email,
        },
        items: this.books.map((book) => ({
          book_id: book.book_id,
          name: book.name,
          image: book.image,
          author: book.author,
          quantity: book.quantity,
          price: book.quantity * book.price,
        })),
        totalPrice: this.totalPrice,
      })
      this.orderStatus = 'success'
      this.updateCart([])
    } catch (error) {
      this.orderStatus = 'error'
      return `Error to confirm order: ${error}`
    }
  },
  methods: {
    ...mapMutations({
      updateCart: 'cart/updateCart',
    }),
  },
}
</script>

<style scoped>
.order-section {
  display: flex;
  justify-content: center;
  color: white;
  margin: 30px;
}
.btn-orders {
  display: flex;
  justify-content: center;
  padding-top: 20px;
  margin-bottom: 20px;
}
</style>
