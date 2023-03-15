module.exports = {
  plugins: ['security'],
  extends: ['eslint:recommended', 'plugin:security/recommended-legacy'],
  rules: {
    'security/detect-eval-with-expression': 'error',
    'security/detect-non-literal-require': 'warn',
    'security/detect-child-process': 'error',
    'security/detect-non-literal-fs-filename': 'warn',
    'security/detect-possible-timing-attacks': 'warn',
  },
};
