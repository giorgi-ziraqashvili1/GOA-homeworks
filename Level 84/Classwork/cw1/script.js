let h1 = document.querySelector("h1")

let h2 = document.querySelector("h2")




document.addEventListener("click", function (event) {
    console.log(event.target)
    
})

h1.addEventListener("click", function () {
    h1.style.color = "red"
})

h2.addEventListener("click", function () {
    h2.style.color = "red"
})
