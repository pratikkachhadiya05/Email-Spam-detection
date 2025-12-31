// JavaScript for dynamic content changes in Spam Email Detector

document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const predictionDiv = document.querySelector('h2') || document.createElement('h2');
    const container = document.querySelector('.container');

    // If prediction h2 doesn't exist, create it
    if (!document.querySelector('h2:last-of-type')) {
        container.appendChild(predictionDiv);
    }

    form.addEventListener('submit', function(e) {
        e.preventDefault(); // Prevent default form submission

        const emailText = document.getElementById('email').value;

        // Send AJAX request
        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: new URLSearchParams({
                'email': emailText
            })
        })
        .then(response => response.json())
        .then(data => {
            if (data.prediction) {
                predictionDiv.textContent = 'Prediction: ' + data.prediction;
            } else {
                predictionDiv.textContent = 'Error: Could not get prediction';
            }
        })
        .catch(error => {
            console.error('Error:', error);
            predictionDiv.textContent = 'Error: Failed to check email';
        });
    });

    // Clear button functionality
    const clearBtn = document.getElementById('clearBtn');
    clearBtn.addEventListener('click', function() {
        document.getElementById('email').value = '';
        predictionDiv.textContent = '';
    });
});