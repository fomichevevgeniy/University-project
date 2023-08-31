const lang = document.querySelector('.dropdown-btn')
const dropLang = document.querySelector('.dropdown-content')
const DropContentTwo = document.getElementById('DropContentTwo')
const dropdown = document.getElementById('dropdown-lang-btn')
const dropdown_btn_one = document.getElementById('dropdown-btn-one')
const dropdown_content_one = document.getElementById('dropdown_content_one')
const window_model = document.querySelector('.document-release')
const close_window = document.querySelector('.document-check-btn')
const news_link = document.querySelectorAll('.news-link-nav')
dropdown_btn_one.addEventListener('click', () => {
    dropdown_content_one.classList.toggle('active')
})
for (let i = 0; i < news_link.length; i++) {
    setTimeout(() => {
        news_link[i].addEventListener('click', function () {
            news_link.forEach(d => d.classList.remove('active'))
            this.classList.add('active')
        })
    }, 100);
}
const media_link = document.querySelectorAll('.media_link')
const media_btn = document.querySelector('.media_btn')
const media_menu = document.querySelector('.media_menu')
const nav_open = document.querySelector('.nav_open-btn')
for (let i = 0; i < media_link.length; i++) {
    setTimeout(() => {
        media_link[i].addEventListener('click', function () {
            media_link.forEach(d => d.classList.remove('active'))
            this.classList.add('active')
        })
    }, 100);
}
media_btn.addEventListener("click", () => {
    media_menu.classList.remove("active");
})
nav_open.addEventListener("click", () => {
    media_menu.classList.add("active");
})

let doc = document.querySelector('.doc')
let three = document.getElementById('media_list-two')
doc.addEventListener('click', function () {
    three.classList.toggle('active')
})

disabled_btn.addEventListener("click", () => {
    window_model.classList.add('active')
})
close_window.addEventListener("click", () => {
    window_model.classList.remove('active')
})

