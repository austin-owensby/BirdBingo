let drawHistory = [];

function drawBird() {
    toggleLoadingButtons(true);

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
            drawHistory.push(newDrawHistory);
        })
        .catch(error => {
            const errorMessage = document.getElementById('error-message');
            errorMessage.innerHTML = error;
        })
        .finally(() => {
            toggleLoadingButtons(false);
            toggleListLoading(false);
        });
}

function fetchDrawHistory() {
    toggleListLoading(true);
    toggleLoadingButtons(true);

    fetch('/api/draw-history', { method: 'GET'})
        .then(response => {
            if (!response.ok) {
                return response.text().then(error_message => {
                    throw new Error(error_message ?? response.statusText);
                })
            }
            return response.json();
        })
        .then(allDrawHistory => {
            drawHistory = allDrawHistory;
        })
        .catch(error => {
            const errorMessage = document.getElementById('error-message');
            errorMessage.innerHTML = error;
        })
        .finally(() => {
            toggleLoadingButtons(false);
            toggleListLoading(false);
        });
}

function startNewGame() {
    toggleListLoading(true);
    toggleLoadingButtons(true);

    fetch('/api/new-game', { method: 'POST'})
        .then(response => {
            if (!response.ok) {
                return response.text().then(error_message => {
                    throw new Error(error_message ?? response.statusText);
                })
            }
            return;
        })
        .then(() => {
            drawHistory = [];
        })
        .catch(error => {
            const errorMessage = document.getElementById('error-message');
            errorMessage.innerHTML = error;
        })
        .finally(() => {
            toggleLoadingButtons(false);
            toggleListLoading(false);
        });
}

function toggleLoadingButtons(loading) {
    const drawBirdButton = document.getElementById('draw-bird');
    drawBirdButton.disabled = loading;

    const newGameButton = document.getElementById('new-game');
    newGameButton.disabled = loading;

    // Clear the error, potentially move this to a toast message that's timed
    if (loading) {
        const errorMessage = document.getElementById('error-message');
        errorMessage.innerHTML = '';
    }
}

function toggleListLoading(loading) {
    const drawHistoryList = document.getElementById('draw-history');

    if (loading) {
        drawHistoryList.innerHTML = 'Loading...';
    }
    else {
        let listHTML = '';

        for (let drawHistoryItem of drawHistory) {
            listHTML += `<li>${drawHistoryItem}</li>`;
        }

        drawHistoryList.innerHTML = listHTML;
    }
}

window.onload = function() {
    const drawBirdButton = document.getElementById('draw-bird');
    drawBirdButton.addEventListener('click', drawBird);

    const newGameButton = document.getElementById('new-game');
    newGameButton.addEventListener('click', startNewGame);

    fetchDrawHistory();
}
