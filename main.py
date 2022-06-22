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
cur.execute("select * from junio14;")
filas = cur.fetchall()
print(filas)
cur.close()
conn.close()



@app.route("/login",methods=["POST"])
def login_post():
    json = request.get_json()
    print(request.form)
    correo = json["user"]
    clave = json["pass"]
    print(correo, clave)
    for i in filas:
        if correo == i[0]:
            if clave==i[1]:
                print("VALIDO")
                return jsonify({"valido":1})
            else:
                print("No VALIDO")
                return jsonify({"valido":0})
    print("No VALIDO")
    return jsonify({"valido":0})

@app.route("/login",methods=["GET"])
def login_get():
    return login_render
        

app.run(port=8080, debug=True)