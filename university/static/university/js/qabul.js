const slider_logo = document.querySelectorAll('.acceptance-slider-img')
const window_logo = document.querySelector(".acceptance-window-logo")
const window_blog = document.querySelector('.acceptance-window')
const window_close_icon = document.querySelector('.acceptance-window-icon')
slider_logo.forEach(el => {
    el.addEventListener("dblclick", () => {
        let imgLogo = el.getAttribute("src")
        window_blog.classList.add('active')
        window_logo.setAttribute("src", imgLogo)
    })
});

window_close_icon.addEventListener('click', () => {
    window_blog.classList.remove('active')
})

const acceptance_logo = document.querySelectorAll('.acceptance-static-blog-logo')

acceptance_logo.forEach(el => {
    el.addEventListener("dblclick", () => {
        let imgLogo = el.getAttribute("src")
        window_blog.classList.add('active')
        window_logo.setAttribute("src", imgLogo)
    })
});