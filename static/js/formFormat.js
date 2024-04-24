document.addEventListener('DOMContentLoaded', function() {
    const phoneInputs = document.querySelectorAll('.phone');
    
    phoneInputs.forEach(function(phoneNumberInput) {
        let isBackspacePressed = false;

        phoneNumberInput.addEventListener('keydown', function(event) {
            // Проверяем, была ли нажата клавиша Backspace
            isBackspacePressed = event.key === 'Backspace';
        });

        phoneNumberInput.addEventListener('input', function() {
            let inputValue = phoneNumberInput.value.replace(/[^\d]/g, ''); // Оставляем только цифры

            if (isBackspacePressed) {
                // Если нажата клавиша Backspace, удаляем соответствующий символ из форматированного номера
                inputValue = inputValue.substring(0, inputValue.length - 1);
                isBackspacePressed = false;
            }

            // Ограничиваем количество символов
            inputValue = inputValue.slice(0, 11);

            // Применяем формат только если введены цифры
            if (/^\d+$/.test(inputValue)) {
                const formattedValue = formatPhoneNumber(inputValue);
                phoneNumberInput.value = formattedValue;
            }
        });

        function formatPhoneNumber(inputNumber) {
            // Применяем формат: +7 (XXX) XXX-XX-XX
            return `+7${inputNumber.slice(1, 4) ? ' (' + inputNumber.slice(1, 4) + ')' : ''}${inputNumber.slice(4, 7) ? ' ' + inputNumber.slice(4, 7) : ''}${inputNumber.slice(7, 9) ? '-' + inputNumber.slice(7, 9) : ''}${inputNumber.slice(9) ? '-' + inputNumber.slice(9) : ''}`;
        }
        
    });
});
