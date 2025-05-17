let drawHistory = [];

function drawBird() {
    fetch('/api/draw-bird', { method: 'POST'})
        .then(response => {
            if (!response.ok) {
                return response.text().then(error_message => {
                    throw new Error(error_message ?? response.statusText);
                })
            }
            return response.text();
        })
        .then(newDrawHistory => {
            const drawHistoryList = document.getElementById('draw-history');

            drawHistory.push(newDrawHistory);

            let listHTML = '';

            for (let drawHistoryItem of drawHistory) {
                listHTML += `<li>${drawHistoryItem}</li>`;
            }

            drawHistoryList.innerHTML = listHTML;
        })
        .catch(error => {
            const errorMessage = document.getElementById('error-message');
            errorMessage.innerHTML = error;
        }
    );
}

window.onload = function() {
    const drawBirdButton = document.getElementById('draw-bird');
    drawBirdButton.addEventListener('click', drawBird);
}
