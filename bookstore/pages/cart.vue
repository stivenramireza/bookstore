<template>
  <v-row class="expansion-panels-container">
    <v-expansion-panels v-model="panel">
      <v-expansion-panel>
        <v-expansion-panel-header color="blue-grey darken-4 white--text">
          1. Cart list
          <template #actions>
            <v-icon color="white"> $expand </v-icon>
          </template>
        </v-expansion-panel-header>
        <v-expansion-panel-content color="blue-grey darken-3 white--text">
          <CartList />
        </v-expansion-panel-content>
      </v-expansion-panel>
    </v-expansion-panels>
    <v-row class="mt-2 btn-pay">
      <v-btn
        tile
        color="blue-grey darken-4 white--text"
        @click="$router.push('/login')"
      >
        <v-icon color="white" left> mdi-currency-usd </v-icon>
        Buy
      </v-btn>
    </v-row>
  </v-row>
</template>

<script>
import CartList from '@/components/common/CartList'
import { mapGetters } from 'vuex'

export default {
  components: {
    CartList,
  },
  data() {
    return {
      panel: 0,
      digitalMineDomain: process.env.DIGITAL_MINE_DOMAIN,
      wompiPublicKey: process.env.WOMPI_PUBLIC_KEY,
    }
  },
  head() {
    return {
      script: [
        {
          src: 'https://checkout.wompi.co/widget.js',
        },
      ],
    }
  },
  computed: {
    ...mapGetters({
      totalPrice: 'cart/totalPrice',
    }),
  },
}
</script>

<style>
.expansion-panels-container {
  margin: 50px;
}
.btn-pay {
  display: flex;
  justify-content: center;
  padding-top: 20px;
  margin-bottom: 20px;
}
.v-select > .v-input__control > .v-input__slot {
  width: 50px;
}
.theme--light.v-application {
  background-color: #263238;
}

.theme--light.v-list {
  background: #263238;
}
.v-list-item__content {
  color: white;
}
.theme--light.v-list-item:hover:before {
  opacity: 0.14;
}
@media (min-width: 320px) and (max-width: 767px) {
  .expansion-panels-container {
    margin: 20px;
  }
}
</style>
