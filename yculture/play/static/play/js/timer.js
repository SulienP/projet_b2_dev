function updateTimer(){
    let countdownElement = document.getElementById("countdown")
    let seconds = 30
    function countdown(){
        seconds--
        let minutes = Math.floor(seconds / 60)
        let remainingSeconds = seconds % 60
        countdownElement.textContent = minutes + ":" + (remainingSeconds < 10 ? "0" : "") + remainingSeconds
        if(seconds <= 0){
            clearInterval(timer)
            countdownElement.textContent = "0:00"
        }
    }
    countdown()
    let timer = setInterval(countdown, 1000)
}

updateTimer()
