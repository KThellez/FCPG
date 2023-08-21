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

var botonesCerrar = document.querySelectorAll('.cerrar_alerta');
botonesCerrar.forEach(function(boton) {
    boton.addEventListener('click', function() {
        this.parentNode.style.display = 'none';
    });
});


var alerta = document.querySelector('.alerta');
var botonCerrar = document.querySelector('.cerrar_alerta');
var tiempoCierre = 3000; // 3 seg
var tiempoID;

botonCerrar.addEventListener('click', function() {
    cerrarAlerta();
});

alerta.addEventListener('mouseenter', reiniciarContador);
alerta.addEventListener('mouseleave', iniciarContador);

iniciarContador();

function iniciarContador() {
    tiempoID = setTimeout(function() {
        cerrarAlerta();
    }, tiempoCierre);
}

function reiniciarContador() {
    clearTimeout(tiempoID);
}

function cerrarAlerta() {
    alerta.style.opacity = '0';
    setTimeout(function() {
        alerta.style.display = 'none';
    }, 300); // 0.3 segundos
}