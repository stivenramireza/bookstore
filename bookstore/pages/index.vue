<template>
  <v-container fluid ma-0 pa-0 fill-heigth color="blue-grey darken-4">
    <v-row class="cards-container">
      <v-col
        v-for="(item, index) in $options.json.books"
        :key="index"
        cols="12"
        md="3"
        sm="6"
      >
        <CardBook :book="item" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import CardBook from '@/components/common/CardBook'
import api from '@/assets/json/api.json'

export default {
  json: api,
  components: {
    CardBook,
  },
}
</script>

<style scoped>
.cards-container {
  margin: 10px;
}
</style>
