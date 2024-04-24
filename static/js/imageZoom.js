document.addEventListener('DOMContentLoaded', function() {
    // Получаем все элементы с классом .image-container
    var imageContainers = document.querySelectorAll('.image-container');
  
    // Добавляем слушатель события 'click' к каждому элементу
    imageContainers.forEach(function(imageContainer) {
      imageContainer.addEventListener('click', function() {
        // Добавляем или удаляем класс zoom__active для текущего элемента
        this.classList.toggle('zoom__active');
      });
    });
  });
  