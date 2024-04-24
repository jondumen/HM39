document.addEventListener('DOMContentLoaded', function() {
    // Encuentra el elemento <html>
    const htmlElement = document.querySelector('html');
    
    // Encuentra el botón de cambio de tema
    const themeToggleButton = document.getElementById('theme-toggle');

    // Agrega un evento de clic al botón de cambio de tema
    themeToggleButton.addEventListener('click', function() {
        // Obtiene el valor actual del atributo data-bs-theme
        const currentTheme = htmlElement.getAttribute('data-bs-theme');

        // Cambia el tema
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        htmlElement.setAttribute('data-bs-theme', newTheme);

        // Cambia las clases de los iconos
        const icons = document.querySelectorAll('.icon');
        icons.forEach(icon => {
            if (newTheme === 'light') {
                icon.classList.add('white-icon');
            } else {
                icon.classList.remove('white-icon');
            }
        });
    });
});
