document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('http://localhost:5001/save', {  // Ensure the URL matches your server
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        // To redirect to new site for user to submit their hobby preferences
        window.location.href = 'preferences.html';
    })
    .catch((error) => {
        console.error('Error:', error);
    });

});