from flask import Flask, render_template, request, redirect, url_for
import redis

app = Flask(_name_)
db = redis.StrictRedis(host="localhost", port=6379, db=0)

@app.route('/')
def index():
    palabras = {}
    for palabra, definicion in db.hgetall('palabras').items():
        palabras[palabra.decode()] = definicion.decode()

    return render_template('index.html', palabras=palabras, db=db)

@app.route("/agregar", methods=["POST"])
def agregar_palabra():
    palabra = request.form["palabra"]
    definicion = request.form["definicion"]
    db.hset("palabras", palabra, definicion)
    return redirect(url_for("index"))

@app.route("/editar", methods=["POST"])
def editar_palabra():
    palabra = request.form["palabra"]
    definicion = request.form["definicion"]
    db.hset("palabras", palabra, definicion)
    return redirect(url_for("index"))

@app.route("/eliminar", methods=["POST"])
def eliminar_palabra():
    palabra = request.form["palabra"]
    db.hdel("palabras", palabra)
    return redirect(url_for("index"))

if _name_ == "_main_":
    app.run(debug=True)