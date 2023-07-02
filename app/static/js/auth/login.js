(function (){
    // Crear elemento de mensaje de carga
    var loadingMessage = document.createElement('div');
    loadingMessage.innerText = 'Cargando...';
    loadingMessage.style.position = 'fixed';
    loadingMessage.style.top = '50%';
    loadingMessage.style.left = '50%';
    loadingMessage.style.transform = 'translate(-50%, -50%)';
    loadingMessage.style.backgroundColor = 'var(--background-tarjetas-temas-user)';
    loadingMessage.style.padding = '10px';
    loadingMessage.style.fontFamily = 'var(--spline-mono-sans)';
    loadingMessage.style.fontSize = '20px';
    loadingMessage.style.fontWeight = 'bold';

    // Mostrar mensaje de carga al inicio
    document.body.appendChild(loadingMessage);

    // Ocultar mensaje de carga cuando la página haya cargado
    document.addEventListener('DOMContentLoaded', function() {
        loadingMessage.style.display = 'none';
    });
})();