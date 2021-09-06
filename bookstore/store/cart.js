export const state = () => ({
  books: [],
})

export const mutations = {
  addItem(state, payload) {
    const existsBook = state.books.find(
      (book) => book.book_id === payload.book_id
    )
    if (existsBook) {
      state.books = state.books.map((book) =>
        book.book_id === payload.book_id
          ? {
              ...existsBook,
              quantity: existsBook.quantity + 1,
            }
          : book
      )
    } else {
      state.books = [...state.books, { ...payload, quantity: 1 }]
    }
  },
  removeItem(state, payload) {
    const existsBook = state.books.find(
      (book) => book.book_id === payload.book_id
    )
    if (existsBook.quantity === 1) {
      state.books = state.books.filter(
        (book) => book.book_id !== payload.book_id
      )
    } else {
      state.books = state.books.map((book) =>
        book.book_id === payload.book_id
          ? {
              ...existsBook,
              quantity: existsBook.quantity - 1,
            }
          : book
      )
    }
  },
}

export const getters = {
  totalPrice: (state) => {
    return state.books.reduce(
      (acc, { price, quantity }) => acc + price * quantity,
      0
    )
  },
}
