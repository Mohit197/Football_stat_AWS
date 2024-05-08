function validatePassword() {
    var passwordInput = document.getElementById("password");
    var errorElement = document.querySelector('.error');
    var usernameInput = document.getElementById("username");
    
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
        }
    };
    xhr.send();
    
    // Prevent form submission
    return false;
}