export const state = () => ({
  books: [],
})

export const mutations = {
  add(state, book) {
    book.selected = true
    state.books.push(book)
  },
  remove(state, payload) {
    payload.selected = false
    state.books = state.books.filter((book) => book.id !== payload.id)
  },
  updateCart(state, payload) {
    state.books.forEach((book) => {
      if (book.book_id === payload.book_id) {
        book.quantity = payload.quantity
        book.price *= book.quantity
      }
    })
  },
}

export const getters = {
  totalPrice: (state) => {
    return state.books.reduce((acc, { price }) => acc + price, 0)
  },
}
