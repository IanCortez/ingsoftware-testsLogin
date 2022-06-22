from flask import Flask, jsonify, render_template, request
import psycopg2

app = Flask(__name__)

with app.app_context(), app.test_request_context():
    login_render = render_template("login.html")



conn = psycopg2.connect(
    host="localhost",
    database="trucos",
    user="postgres",
    password="icg28122002"
)
cur = conn.cursor()
cur.execute("select * from junio14 ORDER BY correo ASC;")
filas = cur.fetchall()
print(filas)
cur.close()
conn.close()


def busqueda_bianria(correo, clave):
    l = 0
    r = len(filas)
    while l < r:
        mid = (l+r)//2
        if filas[mid][0] > correo:
            l = mid + 1
        elif filas[mid][0] < correo:
            r = mid-1
        elif filas[mid][0] == correo:
            if clave == filas[mid][1]:
                return jsonify({"valido":1})
            else:
                return jsonify({"valido":-1})
    return jsonify({"valido":0})


@app.route("/login",methods=["POST"])
def login_post():
    json = request.get_json()
    correo = json["user"]
    clave = json["pass"]
    if len(clave) == 0 or len(correo) == 0:
        return jsonify({"valido": -2})
    
    res = busqueda_bianria(correo, clave)
    return res

@app.route("/login",methods=["GET"])
def login_get():
    return login_render
        

app.run(port=8080, debug=True)