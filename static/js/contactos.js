function abrirAgregar() {
    document.getElementById("formModal").action = "/agregar"
    document.getElementById("id").value = ""
    document.getElementById("dni").value = ""
    document.getElementById("nombre").value = ""
    document.getElementById("telefono").value = ""
    document.getElementById("correo").value = ""
    document.getElementById("direccion").value = ""
    document.getElementById("estado").value = "Activo"
    document.getElementById("modal").style.display = "flex"
}

function abrirEditar(id, dni, nombre, telefono, correo, direccion, estado) {
    document.getElementById("formModal").action = "/editar"
    document.getElementById("id").value = id
    document.getElementById("dni").value = dni
    document.getElementById("nombre").value = nombre
    document.getElementById("telefono").value = telefono
    document.getElementById("correo").value = correo
    document.getElementById("direccion").value = direccion
    document.getElementById("estado").value = estado
    document.getElementById("modal").style.display = "flex"
}

function cerrarModal() {
    document.getElementById("modal").style.display = "none"
}
