function validatePassword() {
    var passwordInput = document.getElementById("password");
    var errorElement = document.querySelector('.error');
    var usernameInput = document.getElementById("username");
    var nameInput = document.getElementById("name");
    var ageInput = document.getElementById("age");

    // Reset error message
    errorElement.textContent = "";
    errorElement.classList.add('error--hidden');

    
    // Check name validity
    var name = nameInput.value.trim();
    var nameRegex = /^[A-Za-z\s]+$/;
    if (!nameRegex.test(name)) {
        errorElement.textContent = "Name must contain only letters and spaces.";
        errorElement.classList.remove('error--hidden');
        return false;
    }

    
    // Check age validity
    var age = parseInt(ageInput.value, 10);
    if (isNaN(age) || age < 0 || age > 70) {
        errorElement.textContent = "Age must be a valid number and not more than 70.";
        errorElement.classList.remove('error--hidden');
        return false;
    }

    // Check password length
    if (passwordInput.value.length < 8) {
        errorElement.textContent = "Password must be at least 8 characters long.";
        errorElement.classList.remove('error--hidden');
        return false;
    }

    // Check if user already exists
    var username = usernameInput.value.trim();
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/check_user_exists?username=' + username, true);
    xhr.onload = function() {
        if (xhr.status === 200) {
            var response = JSON.parse(xhr.responseText);
            if (response.exists) {
                errorElement.textContent = "Username already exists. Please choose a different one.";
                errorElement.classList.remove('error--hidden');
            } else {
                // If user doesn't exist, submit the form
                document.forms[0].submit();
            }
        } else {
            errorElement.textContent = "Error checking username. Please try again.";
            errorElement.classList.remove('error--hidden');
        }
    };
    xhr.onerror = function() {
        errorElement.textContent = "Error: Request failed.";
        errorElement.classList.remove('error--hidden');
    };
    xhr.send();
    
    // Prevent form submission until AJAX call completes
    return false;
}
