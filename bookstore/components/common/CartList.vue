<template>
  <v-list color="blue-grey darken-3">
    <div v-if="items.length > 0">
      <v-list-item>
        <v-list-item-avatar></v-list-item-avatar>
        <v-list-item-title class="product"
          ><strong>Book</strong></v-list-item-title
        >
        <v-list-item-title><strong>Quantity</strong></v-list-item-title>
        <v-list-item-title><strong>Summary</strong></v-list-item-title>
      </v-list-item>
      <v-list-item v-for="(item, index) in items" :key="index" color="white">
        <v-list-item-avatar>
          <v-img :src="item.image"></v-img>
        </v-list-item-avatar>
        <v-list-item-title class="product" style="width: 10px">
          {{ item.name }}</v-list-item-title
        >
        <v-list-item-title>
          <v-btn
            v-if="isCart"
            color="white"
            text
            @click="removeItem(item) + $forceUpdate()"
          >
            <v-icon left>mdi-minus</v-icon>
          </v-btn>

          {{ item.quantity }}
          <v-btn
            v-if="isCart"
            color="white"
            text
            @click="addItem(item) + $forceUpdate()"
          >
            <v-icon left>mdi-plus</v-icon>
          </v-btn>
        </v-list-item-title>
        <v-list-item-title
          >{{ item.quantity }} units x
          {{ item.price | priceFormat }}</v-list-item-title
        >
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
    </div>
    <div v-else>
      <v-list-item-title class="white--text">Cart is empty</v-list-item-title>
    </div>
  </v-list>
</template>

<script>
export default {
  props: {
    isCart: {
      type: Boolean,
      default: true,
    },
    items: {
      type: Array,
      default: () => [],
    },
    totalPrice: {
      type: Number,
      default: 0,
    },
    addItem: {
      type: Function,
      default: () => null,
    },
    removeItem: {
      type: Function,
      default: () => null,
    },
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
