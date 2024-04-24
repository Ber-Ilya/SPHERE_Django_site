document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        var bedroomControlElement = document.querySelector('.bedroom__control');
        if (bedroomControlElement) {
            bedroomControlElement.classList.add('__active');
        }
    }, 100);
});
