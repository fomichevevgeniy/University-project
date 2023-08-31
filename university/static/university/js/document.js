const disabled_btn = document.querySelector(".document-send-information")
const window_model_id = document.getElementById('release')
disabled_btn.addEventListener('click', () => {
    window_model_id.classList.add('active')
})

const document_upload = document.querySelector('.document-img-upload')



const img_input = document.getElementById('img_input') // img id


const imgInp = document.querySelector('#input_images_front')
const blah = document.querySelector('#blah')

imgInp.onchange = evt => {
    const [file] = imgInp.files
    if (file) {
        blah.src = URL.createObjectURL(file)
    }
}

const imgInp2 = document.querySelector('#input_images_back')
const blah2 = document.querySelector('#blah2')

imgInp2.onchange = evt => {
    const [file] = imgInp2.files
    if (file) {
        blah2.src = URL.createObjectURL(file)
    }
}
