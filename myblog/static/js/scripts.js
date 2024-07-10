const mode = document.getElementById("base-header");
const username = document.getElementById("username");
const password = document.getElementById("password");
const email = document.getElementById("email");
const login = document.querySelector(".login");
const register = document.querySelector(".register");
const content = document.querySelector(".content");
const backgroundImage = document.querySelector(".image-container");

const body = document.body;

function cambiarModo() {
  mode.classList.toggle("dark-page-header");
  if (backgroundImage) backgroundImage.classList.toggle("dark-mode-img");

  if (username) username.classList.toggle("dark-mode-input");
  if (password) password.classList.toggle("dark-mode-input");
  if (email) email.classList.toggle("dark-mode-input");

  body.classList.toggle("dark-mode");
  if (content) content.classList.toggle("dark-mode");
  if (login) login.classList.toggle("dark-mode");
  if (register) register.classList.toggle("dark-mode");

  // Guardar estado del modo en localStorage
  if (body.classList.contains("dark-mode")) {
    localStorage.setItem("mode", "dark");
  } else {
    localStorage.setItem("mode", "light");
  }
}

// Cargar estado del modo desde localStorage
function cargarModo() {
  const savedMode = localStorage.getItem("mode");
  if (savedMode === "dark") {
    mode.classList.add("dark-page-header");

    if (backgroundImage) backgroundImage.classList.add("dark-mode-img");

    if (username) username.classList.add("dark-mode-input");
    if (password) password.classList.add("dark-mode-input");
    if (email) email.classList.add("dark-mode-input");
    body.classList.add("dark-mode");
    if (content) content.classList.add("dark-mode");
    if (login) login.classList.add("dark-mode");
  }
}

$(document).ready(function () {
  // Llama a cargarModo cuando el documento está listo
  cargarModo();

  $(".toggle-mode-btn").click(() => {
    $(".register").toggleClass("dark-mode");
  });
});
