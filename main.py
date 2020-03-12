from flask import Flask, render_template,request, make_response, redirect
import random
from funciones import isEntero, datosCorrectosEntrada, datosCorrectosJuego

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        usuario = request.cookies.get("user_name")
        if usuario:
            user_name = usuario
        else:
            user_name = ""
        return render_template("index.html", user_name=user_name, mostrar="none", mensaje="")
    elif request.method == "POST":
        nombre = request.form.get("user-name")
        l_minimo = request.form.get("minimo")
        l_maximo = request.form.get("maximo")
        mensaje_error = "ERROR: los límites deben ser números enteros y el limite inferior debe ser menor que el límite superior"

        if datosCorrectosEntrada(l_minimo, l_maximo):   # los valores que se introducen son string
            response = make_response(redirect("/juego"))
            response.set_cookie("user_name", nombre)
            response.set_cookie("l_minimo", l_minimo)
            response.set_cookie("l_maximo", l_maximo)
            response.set_cookie("secret_number", str(random.randint(int(l_minimo), int(l_maximo))))
            return response
        else:
            return render_template("index.html", mostrar="true", mensaje=mensaje_error, user_name=nombre)


@app.route("/juego", methods=["POST", "GET"])
def juego():
    """"
    print(request.cookies.get("user_name"))
    print(request.cookies.get("l_minimo"))
    print(request.cookies.get("l_maximo"))
    print(request.cookies.get("secret_number"))
    """

    if request.method == "GET":
        return render_template("juego.html", minimo=request.cookies.get("l_minimo"), maximo=request.cookies.get("l_maximo"), mostrar="none", mensaje="")
    elif request.method == "POST":
        usuario = request.cookies.get("user_name")
        secreto = int(request.cookies.get("secret_number"))   # Ya se sabe que es numérico
        apuesta = request.form.get("guess")
        minimo = request.cookies.get("l_minimo")
        maximo = request.cookies.get("l_maximo")

        if datosCorrectosJuego(apuesta, minimo, maximo):
            if secreto == int(apuesta):
                response = make_response(render_template("success.html", user_name=usuario))
                response.set_cookie("user_name", expires=0)
                response.set_cookie("l_minimo", expires=0)
                response.set_cookie("l_maximo", expires=0)
                response.set_cookie("secret_number", expires=0)
                return response
            elif secreto < int(apuesta):
                mensaje_info = "WARNING: su apuesta es mayor que el número secreto. Inténtelo otra vez."
            else:   # el numero secreto es mayor
                mensaje_info = "WARNING: su apuesta es menor que el número secreto. Inténtelo otra vez."

            return render_template("juego.html", mostrar="true", mensaje=mensaje_info, minimo=minimo, maximo=maximo)
        else:
            mensaje_info = "ERROR: la apuesta debe ser un valor numérico y estar comprendido entre los límites"
            return render_template("juego.html", mostrar="true", mensaje=mensaje_info, minimo=minimo, maximo=maximo)




if __name__ == '__main__':
    app.run(debug="True")
