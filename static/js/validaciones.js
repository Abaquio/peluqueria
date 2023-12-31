function validarFormulario() {
    var nombre = document.getElementById('nombre').value;
    var apellido = document.getElementById('apellido').value;
    var correo = document.getElementById('correo').value;
    var fono = document.getElementById('fono').value;
    // var servicio = document.getElementById('servicios').value;

    
    //Validar Nombre
    if (nombre.length < 3 || nombre.length > 20) {
        document.getElementById('nombre_msj').innerHTML = 'El nombre debe tener entre 3 y 20 caracteres.';
        return false;
        
    } else {
        document.getElementById('nombre_msj').innerHTML = '';
    }

    //Validar Apellido
    if (apellido.length < 3 || apellido.length > 20) {
        document.getElementById('apellido_msj').innerHTML = 'El apellido debe tener entre 3 y 20 caracteres.';
        return false;
    } else {
        document.getElementById('apellido_msj').innerHTML = '';
    }

    //Validar Correo
    if (!validarCorreo(correo)) {
        document.getElementById('correo_msj').innerHTML = 'Ingrese un correo electrónico válido.';
        return false;
    } else {
        document.getElementById('correo_msj').innerHTML = '';
    }

    //Validar Telefono
    if (!validarfono(fono)) {
        document.getElementById('fono_msj').innerHTML = 'Ingrese un número de teléfono válido.';
        return false;
    } else {
        document.getElementById('fono_msj').innerHTML = '';
    }

    //Validar Servicio
    // if (servicio === 'Elija una opcion') {
    //     document.getElementById('servicios_msj').innerHTML = 'Seleccione un servicio válido.';
    //     return false;
    // } else {
    //     document.getElementById('servicios_msj').innerHTML = '';
    // }
    // return true;
}

function validarCorreo(correo) {
    var regexCorreo = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regexCorreo.test(correo);
}

function validarfono(fono) {
    var regexfono = /^\d+([\s\-]?\d+)*$/;
    return regexfono.test(fono);
}