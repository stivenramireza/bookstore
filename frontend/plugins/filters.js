import Vue from 'vue'
import numeral from 'numeral'

Vue.filter('priceFormat', (value) => {
  return '$' + numeral(value).format('0,0,0,0,0')
})
