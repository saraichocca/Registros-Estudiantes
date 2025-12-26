from flask import Flask, render_template, request, redirect
from conexion import obtener_conexion

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/guardar', methods=['POST'])
def guardar():
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    ciudad = request.form['ciudad']

    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO estudiantes (nomEstudiante, dirEstudiante, ciuEstudiante) VALUES (%s, %s, %s)",
            (nombre, direccion, ciudad)
        )
    conexion.commit()
    conexion.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

