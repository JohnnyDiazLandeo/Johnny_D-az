document.getElementById("loginForm").addEventListener("submit", e => {
    e.preventDefault()
    const usuario = document.getElementById("usuario").value
    const password = document.getElementById("password").value

    if (usuario === "admin" && password === "1234") {
        window.location.href = "contactos.html"
    }
})
