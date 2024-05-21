document.addEventListener('DOMContentLoaded', (event) => {
    const form = document.querySelector('#quiz-form');
    const radioButtons = document.querySelectorAll('input[type="radio"]');
    const errorMessage = document.querySelector('#error-message');

    form.addEventListener('submit', (event) => {
        let isChecked = false;
        radioButtons.forEach((radio) => {
            if (radio.checked) {
                isChecked = true;
            }
        });

        if (!isChecked) {
            event.preventDefault();
            errorMessage.innerText = 'Please select an answer before proceeding to the next question.';
            errorMessage.style.display = 'block';
        } else {
            errorMessage.innerText = '';
            errorMessage.style.display = 'none';
        }
    });

    // Store selected choice in session storage
    radioButtons.forEach((radio) => {
        radio.addEventListener('click', (event) => {
            sessionStorage.setItem('lastChoice', event.target.value);
        });
    });

    // Pre-select last choice when navigating back
    const lastChoice = sessionStorage.getItem('lastChoice');
    if (lastChoice) {
        const selectedRadio = document.querySelector(`input[type="radio"][value="${lastChoice}"]`);
        if (selectedRadio) {
            selectedRadio.checked = true;
        }
    }
});