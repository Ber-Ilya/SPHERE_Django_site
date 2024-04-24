function openPopup(selector) {
    const popup = document.querySelector(selector);
    if (popup) {
        popup.style.display = 'block';
    }
}

function closePopup(selector) {
    const popup = document.querySelector(selector);
    if (popup) {
        popup.style.display = 'none';
    }
}
