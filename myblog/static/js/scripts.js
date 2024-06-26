const mode = document.getElementById('base-header')
const username = document.getElementById('username')
const password = document.getElementById('password')
const login = document.querySelector('.login')
const content = document.querySelector('.content')

const body = document.body

function cambiarModo() {
  mode.classList.toggle('dark-page-header')
  //change usernm and passwd colors
  username.classList.toggle('dark-mode-input')
  password.classList.toggle('dark-mode-input')

  body.classList.toggle('dark-mode')
  content.classList.toggle('dark-mode')
  login.classList.toggle('dark-mode')
}
$(document).ready(function(){
  $('.toggle-mode-btn').click(() => {
    $('.register').toggleclass('dark-mode')
  })
})