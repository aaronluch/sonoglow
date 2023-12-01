document.addEventListener('DOMContentLoaded', function() {
    const updateForm = document.getElementById('updateForm'); // Assuming your form has this id

    updateForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission
        callUpdateSong();
    });

    const continuousButton = document.getElementById('continuousButton');
    continuousButton.addEventListener('click', toggleContinuousUpdate);
});

let continuousUpdateEnabled = false;
let updateInterval;

function toggleContinuousUpdate() {
    continuousUpdateEnabled = !continuousUpdateEnabled;
    document.getElementById('continuousButton').innerText = `CONTINUOUS: ${continuousUpdateEnabled ? 'ENABLED' : 'DISABLED'}`;

    if (continuousUpdateEnabled) {
        updateInterval = setInterval(callUpdateSong, 5000); // Call every 5 seconds
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
    .then(response => response.json())
    .then(data => {
        console.log('Update song successful:', data);
        if (data) {
            // Update the web page with the new song info
            document.getElementById('nowPlaying').innerHTML = `Now Playing: ${data.track_name} by ${data.artists}`;
        }
    })
    .catch(error => {
        console.error('Error during update song:', error);
    });
}
