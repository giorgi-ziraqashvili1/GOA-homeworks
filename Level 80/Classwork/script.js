let clockInterval;
        
function updateClock() {
    let now = new Date()
    let time = now.toLocaleTimeString()
    document.getElementById('clock').innerText = time
}

function startClock() {
    if (!clockInterval) {
        updateClock()
        clockInterval = setInterval(updateClock, 1000);
    }
}

function stopClock() {
    clearInterval(clockInterval)
    clockInterval = null
}

startClock();