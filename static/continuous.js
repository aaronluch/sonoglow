let continuousUpdateEnabled = false;
let updateInterval;

function toggleContinuousUpdate() {
    continuousUpdateEnabled = !continuousUpdateEnabled;
    document.getElementById('continuousButton').innerText = `CONTINUOUS: ${continuousUpdateEnabled ? 'ENABLED' : 'DISABLED'}`;

    if (continuousUpdateEnabled) {
        updateInterval = setInterval(callUpdateSong, 5000);
    } else {
        clearInterval(updateInterval);
    }
}

function callUpdateSong() {
    fetch('/updateSong', { 
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        console.log('Update song successful:', data);
    })
    .catch(error => {
        console.error('Error during update song:', error);
    });
}