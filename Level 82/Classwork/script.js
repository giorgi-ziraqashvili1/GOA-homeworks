let hex = "0123456789abcdef";

const btn = document.getElementById("btn")
let Color = document.getElementById("color")
let main = document.querySelector("main")

btn.addEventListener("click", function () {
    let resultColor = "#"

    for (let num = 0; num < 6; num++) {
        let randomIndex = Math.floor(Math.random() * 16)
        resultColor = resultColor + hex[randomIndex]
    }

    Color.textContent = resultColor
    Color.style.color = resultColor
    main.style.backgroundColor = resultColor
    resultColor = "#"
});