module.exports = {
    root: true,
    env: {
      browser: true,
      node: true
    },
    parserOptions: {
      parser: '@typescript-eslint/parser'
    },
    extends: [
      'plugin:vue/recommended',
      'plugin:prettier/recommended'
    ],
    plugins: ['vue'],
    rules: {
      semi: [2, 'never'],
      'no-console': 'off',
      'vue/max-attributes-per-line': 'off',
      'prettier/prettier': ['error', {
        semi: false,
        singleQuote: true
      }]
    }
  };