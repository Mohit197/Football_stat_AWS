document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent default form submission
    
    // Get form data
    var formData = new FormData(this);
    
    // Send AJAX request
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/login", true);
    xhr.setRequestHeader("X-Requested-With", "XMLHttpRequest"); // Set header to indicate AJAX request
    xhr.onload = function() {
        var response = JSON.parse(xhr.responseText);
        if (xhr.status === 200) {
            window.location.href = response.redirect; // Redirect to home page if login is successful
        } else {
            // Display error message
            document.getElementById("loginError").textContent = response.error;
            document.getElementById("loginError").classList.remove("error--hidden");
        }
    };
    xhr.send(formData);
});