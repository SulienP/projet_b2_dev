function handleResponseButtonClick() {
    let buttons = document.querySelectorAll('.response-button')
    buttons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault()
            let selectedAnswer = button.value;
            console.log('Selected answer:', selectedAnswer)

            let formData = new FormData()
            formData.append('selected_answer', selectedAnswer)
            
            fetch('/play/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': '{{ csrf_token }}'
                }
            })
            .then(response => {
                if (response.ok) {
                    console.log('Réponse enregistrée avec succès');
                    // Actualiser la page après avoir envoyé la réponse
                    location.reload()
                } else {
                    console.error('Erreur lors de l\'enregistrement de la réponse')
                }
            })
            .catch(error => {
                console.error('Erreur lors de l\'envoi des données:', error)
            })
        })
    })
}

handleResponseButtonClick()

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
