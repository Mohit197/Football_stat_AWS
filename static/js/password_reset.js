document.getElementById('reset-form').onsubmit = function(event) {
    event.preventDefault(); // Prevent the form from submitting

    const emailInput = document.getElementById('email');
    const errorMessage = document.getElementById('error-message');

    // Clear any previous error message
    errorMessage.style.display = 'none';

    // Check if the email input is empty
    if (emailInput.value.trim() === '') {
        errorMessage.textContent = 'Error: Email cannot be empty.';
        errorMessage.style.display = 'block'; // Show error message
        return;
    }

    // Check for "@" symbol in the email
    if (!emailInput.value.includes('@')) {
        errorMessage.textContent = 'Error: Email must contain "@" symbol.';
        errorMessage.style.display = 'block'; // Show error message
        return;
    }

    // Check if user exists
    const username = emailInput.value.split('@')[0]; // Assuming username is before '@'
    fetch(`/check_user_exists?username=${username}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            if (!data.exists) {
                errorMessage.textContent = 'Error: User does not exist.';
                errorMessage.style.display = 'block'; // Show error message
            } else {
                errorMessage.style.display = 'none'; // Hide error message
                // If user exists, you can submit the form here
                // You might want to proceed to a different page or show a success message
                // For example:
                alert('A password reset link has been sent to your email.');
                // Optionally, you can redirect the user or show a success message
                // this.submit(); // Uncomment to submit the form if you have a backend route for processing
            }
        })
        .catch(err => {
            console.error('Error:', err);
            errorMessage.textContent = 'Error: Something went wrong.';
            errorMessage.style.display = 'block'; // Show error message
        });
};
