/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    //"./profiles/templates/**/*.html", // Added profiles templates to the content list
    './templates/**/*.html',
      './node_modules/flowbite/**/*.js'
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: {"50":"#eff6ff","100":"#dbeafe","200":"#bfdbfe","300":"#93c5fd","400":"#60a5fa","500":"#3b82f6","600":"#2563eb","700":"#1d4ed8","800":"#1e40af","900":"#1e3a8a","950":"#172554"},
        secondary: '#FFFFFF',
        tertiary: '#F2F4F7',
        quaternary: '#141517',
        'primary-dark': '#E44E17', // Added primary-dark color
      },
      fontFamily: {
        sans: ['Rubik', 'sans-serif'],
        serif: ['Lora', 'serif'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'), // Added Tailwind CSS Forms plugin
    require('flowbite/plugin')
  ],
}