/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html', // Scan your template files
    './**/templates/**/*.html', // If using multiple apps
  ],
  theme: {
    extend: {},
  },
  plugins: [],
};
