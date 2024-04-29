// Array of background image URLs
const backgroundImages = [
    'url("/static/Football_Background1.jpg")',
    'url("/static/Football_Background2.jpg")',
    'url("/static/Football_Background3.jpg")',
    'url("/static/Football_Background4.jpg")'
];

// Function to change the background image
function changeBackgroundImage(imageIndex) {
    // Set the background image of the body
    document.body.style.backgroundImage = backgroundImages[imageIndex];
}

// Initialize image index
let currentImageIndex = 0;

// Call the function to change the background image with a specific index
window.onload = function() {
    // Call the function with the initial image index
    changeBackgroundImage(currentImageIndex);

    // Change the background image every 15 seconds
    setInterval(function() {
        // Increment the image index
        currentImageIndex = (currentImageIndex + 1) % backgroundImages.length;
        // Call the function with the updated image index
        changeBackgroundImage(currentImageIndex);
    }, 15000); // 15 seconds in milliseconds
};
