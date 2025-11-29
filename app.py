from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secret_key = "clave"

app.config['MYSQL_HOST'] = "gala2025.cz1gdhkqefmh.us-east-1.rds.amazonaws.com"
app.config['MYSQL_USER'] = "admin"
app.config['MYSQL_PASSWORD'] = "GALACTICO18"
app.config['MYSQL_DB'] = "empresa"

mysql = MySQL(app)

@app.route("/")
def home():
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form["usuario"]
        password = request.form["password"]

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM usuarios WHERE usuario=%s AND password=%s", (usuario, password))
        user = cursor.fetchone()

        if user:
            session["login"] = True
            session["usuario"] = usuario
            return redirect("/contactos")
        else:
            flash("Credenciales incorrectas", "error")

    return render_template("login.html")

def login_requerido(f):
    def wrapper(*args, **kwargs):
        if "login" in session:
            return f(*args, **kwargs)
        return redirect("/login")
    wrapper.__name__ = f.__name__
    return wrapper

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/contactos")
@login_requerido
def contactos():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM clientes")
    data = cursor.fetchall()
    return render_template("contactos.html", clientes=data)

@app.route("/agregar", methods=["POST"])
@login_requerido
def agregar():
    dni = request.form["dni"]
    nombre = request.form["nombre"]
    telefono = request.form["telefono"]
    correo = request.form["correo"]
    direccion = request.form["direccion"]
    estado = request.form["estado"]

    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO clientes(dni, nombre, telefono, correo, direccion, estado)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (dni, nombre, telefono, correo, direccion, estado))
    mysql.connection.commit()

    return redirect("/contactos")

@app.route("/editar", methods=["POST"])
@login_requerido
def editar():
    id = request.form["id"]
    dni = request.form["dni"]
    nombre = request.form["nombre"]
    telefono = request.form["telefono"]
    correo = request.form["correo"]
    direccion = request.form["direccion"]
    estado = request.form["estado"]

    cursor = mysql.connection.cursor()
    cursor.execute("""
        UPDATE clientes
        SET dni=%s, nombre=%s, telefono=%s, correo=%s, direccion=%s, estado=%s
        WHERE id=%s
    """, (dni, nombre, telefono, correo, direccion, estado, id))
    mysql.connection.commit()

    return redirect("/contactos")

@app.route("/eliminar/<int:id>")
@login_requerido
def eliminar(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM clientes WHERE id=%s", (id,))
    mysql.connection.commit()
    return redirect("/contactos")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
