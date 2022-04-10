<template>
  <v-container fluid ma-0 pa-0 fill-heigth color="blue-grey darken-4">
    <v-row v-if="books.length > 0" class="cards-container">
      <v-col
        v-for="(item, index) in books"
        :key="index"
        cols="12"
        md="3"
        sm="6"
      >
        <CardBook :book="item" />
      </v-col>
    </v-row>
    <v-row v-else class="cards-container white--text">
      No hay catálogo disponible...
    </v-row>
  </v-container>
</template>

<script>
import CardBook from '@/components/common/CardBook'

export default {
  components: {
    CardBook,
  },
  async asyncData({ $axios }) {
    try {
      const url = `${process.env.BOOKS_API}/book`
      const data = await $axios.$get(url)
      return {
        books: data,
      }
    } catch (err) {
      return {
        books: [],
      }
    }
  },
}
</script>

<style scoped>
.cards-container {
  margin: 10px;
}
.catalog-section {
  display: flex;
  justify-content: center;
  color: white;
  margin: 30px;
}
</style>
