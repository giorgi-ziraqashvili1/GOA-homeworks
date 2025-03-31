let body = document.body

let parentDiv = document.createElement("div")

let childDiv = document.createElement("div")

let childDiv1 = document.createElement("div")

parentDiv.appendChild(childDiv)
parentDiv.appendChild(childDiv1)
body.appendChild(parentDiv)

body.style.display = "flex"
body.style.height = "100vh"
body.style.alignItems = "center"
body.style.justifyContent = "center"


parentDiv.style.width = "500px"
parentDiv.style.height = "500px"
parentDiv.style.backgroundColor = "blue"
parentDiv.style.display = "flex"
parentDiv.style.justifyContent = "space-between"
parentDiv.style.alignItems = "center"
parentDiv.style.borderRadius = "15px"
parentDiv.style.flexDirection ="column"

childDiv.style.width = "200px"
childDiv.style.height = "200px"
childDiv.style.backgroundColor = "red"
childDiv.style.borderRadius = "10px"

childDiv1.style.width = "200px"
childDiv1.style.height = "200px"
childDiv1.style.backgroundColor = "green"
childDiv1.style.borderRadius = "10px"