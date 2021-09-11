<template>
  <div class="text-center">
    <div v-if="orders.length === 0">
      <p class="orders-section">Getting your orders...</p>
    </div>
    <div v-else>
      <p class="orders-section">My orders</p>
      <v-row class="expansion-panels-container">
        <v-expansion-panels v-model="panel">
          <v-expansion-panel v-for="(item, index) in orders" :key="index">
            <v-expansion-panel-header color="blue-grey darken-4 white--text"
              >Order {{ item.order_id }}
              <template #actions>
                <v-icon color="white"> $expand </v-icon>
              </template>
            </v-expansion-panel-header>
            <v-expansion-panel-content color="blue-grey darken-3 white--text">
              <CartList
                :is-cart="false"
                :items="item.items"
                :total-price="item.totalPrice"
              />
            </v-expansion-panel-content>
          </v-expansion-panel>
        </v-expansion-panels>
      </v-row>
    </div>
  </div>
</template>

<script>
import CartList from '@/components/common/CartList'

export default {
  components: {
    CartList,
  },
  middleware: 'auth',
  data() {
    return {
      panel: 0,
      orders: [],
    }
  },
  async mounted() {
    try {
      const url = `${process.env.ORDERS_API}/orders?email=${this.$auth.user.email}`
      this.orders = await this.$axios.$get(url)
      this.panel = this.orders.length - 1
    } catch (err) {
      return `Error to get orders: ${err}`
    }
  },
}
</script>

<style>
.orders-section {
  display: flex;
  justify-content: center;
  color: white;
  margin: 30px;
}
.expansion-panels-container {
  margin: 50px;
}
@media (min-width: 320px) and (max-width: 767px) {
  .expansion-panels-container {
    margin: 20px;
  }
}
</style>
