// -------- MODALES --------
const modalAgregar = document.getElementById("modalAgregar");
const modalEditar = document.getElementById("modalEditar");

const btnMostrarAgregar = document.getElementById("btnMostrarAgregar");
const btnCerrar = document.querySelectorAll(".cerrarModal");

// ABRIR MODAL AGREGAR
btnMostrarAgregar.addEventListener("click", () => {
    modalAgregar.style.display = "block";
});

// CERRAR MODALES
btnCerrar.forEach(btn => {
    btn.addEventListener("click", () => {
        modalAgregar.style.display = "none";
        modalEditar.style.display = "none";
    });
});


// -------- BOTONES EDITAR --------
const botonesEditar = document.querySelectorAll(".btnEditar");
const formEditar = document.getElementById("formEditar");

botonesEditar.forEach(btn => {
    btn.addEventListener("click", () => {

        const id = btn.dataset.id;

        // Rellena el modal con los datos
        document.getElementById("editDni").value = btn.dataset.dni;
        document.getElementById("editNombre").value = btn.dataset.nombre;
        document.getElementById("editTelefono").value = btn.dataset.telefono;
        document.getElementById("editCorreo").value = btn.dataset.correo;
        document.getElementById("editDireccion").value = btn.dataset.direccion;
        document.getElementById("editEstado").value = btn.dataset.estado;

        // Ruta dinámica
        formEditar.action = `/editar/${id}`;

        // Mostrar modal
        modalEditar.style.display = "block";
    });
});
