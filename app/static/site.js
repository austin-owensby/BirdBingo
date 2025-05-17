let drawHistory = [];
let boards = [];

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

function fetchBoards() {
    fetch('/api/boards', { method: 'GET'})
        .then(response => {
            if (!response.ok) {
                return response.text().then(error_message => {
                    throw new Error(error_message ?? response.statusText);
                })
            }
            return response.json();
        })
        .then(allBoards => {
            boards = allBoards;
        })
        .catch(error => {
            const errorMessage = document.getElementById('error-message');
            errorMessage.innerHTML = error;
        })
        .finally(() => {
            toggleBoardLoading(false);
        });
}

function startNewGame() {
    toggleListLoading(true);
    toggleLoadingButtons(true);
    toggleBoardLoading(true);

    fetch('/api/new-game', { method: 'POST'})
        .then(response => {
            if (!response.ok) {
                return response.text().then(error_message => {
                    throw new Error(error_message ?? response.statusText);
                })
            }
            return response.json();
        })
        .then(newBoards => {
            drawHistory = [];
            boards = newBoards;
        })
        .catch(error => {
            const errorMessage = document.getElementById('error-message');
            errorMessage.innerHTML = error;
        })
        .finally(() => {
            toggleLoadingButtons(false);
            toggleListLoading(false);
            toggleBoardLoading(false);
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

function toggleBoardLoading(loading) {
    const boardList = document.getElementById('boards');

    if (loading) {
        boardList.innerHTML = 'Loading...';
    }
    else {
        let listHTML = '';

        for (let board of boards) {
            listHTML += `<table><caption>${board.owner}</caption><tbody>`;

            for (let i = 0; i < 5; i++) {
                listHTML += '<tr>';

                for (let j = 0; j < 5; j++) {
                    bird = board.grid[i * 5 + j];
                    listHTML += `<td>${bird}</td>`;
                }

                listHTML += '</tr>';
            }

            listHTML += '</tbody></table>';
        }

        boardList.innerHTML = listHTML;
    }
}

window.onload = function() {
    toggleListLoading(true);
    toggleLoadingButtons(true);
    toggleBoardLoading(true);
    
    const drawBirdButton = document.getElementById('draw-bird');
    drawBirdButton.addEventListener('click', drawBird);

    const newGameButton = document.getElementById('new-game');
    newGameButton.addEventListener('click', startNewGame);

    fetchDrawHistory();
    fetchBoards();
}
