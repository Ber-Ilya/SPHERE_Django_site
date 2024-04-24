document.addEventListener('DOMContentLoaded', function () {
    let burgerMenu = document.querySelector('.burger__menu');
    let scrollPosition = 0;
  
    window.addEventListener('scroll', function () {
      let currentScroll = window.pageYOffset;
  
      if (currentScroll > scrollPosition && currentScroll > 100) {
        // Прокрутка вниз более 100 пикселей - добавить класс
        burgerMenu.classList.add('__burger-fixed');
      } else if (currentScroll < 100) {
        // Прокрутка вверх менее 100 пикселей - удалить класс
        burgerMenu.classList.remove('__burger-fixed');
      }
  
      scrollPosition = currentScroll;
    });
  });
  