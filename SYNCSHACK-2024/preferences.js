document.getElementById('hobbiesForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Collect selected industries
    const industries = Array.from(document.querySelectorAll('input[name="industry"]:checked'))
        .map(checkbox => checkbox.value);
    
    // Collect selected hobbies
    const hobbies = Array.from(document.querySelectorAll('input[name="hobbies"]:checked'))
        .map(checkbox => checkbox.value);

    fetch('http://localhost:5001/save_hobbies', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ industries: industries, hobbies: hobbies })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // Redirect to suggested circles
        window.location.href = 'circles.html';
    })
    .catch((error) => {
        console.error('Error:', error);
    });
});
