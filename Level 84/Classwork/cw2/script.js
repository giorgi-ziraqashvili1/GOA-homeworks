

document.querySelector('.container').addEventListener('click', function(event) {

    var box = event.target.closest('.color')

    if (box) {

        var color = box.id

        box.style.backgroundColor = color

        box.querySelector('p').textContent = color

    }
})