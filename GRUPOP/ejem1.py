from flask.helpers import url_for
import pymysql
from flask import Flask,render_template,request,redirect,flash
from datetime import datetime

connection=pymysql.connect(
            host="127.0.0.1", # si es remota coloca IP
            user='root',
            password='newrootpassword',
            db='universidad',)

cursor=connection.cursor()

sql='SELECT * FROM alumnos'
try:
    cursor.execute(sql)
    data=cursor.fetchall() # mas de uno
    print(data)
except Exception as e:
    raise

#################################################333###
#sql='INSERT INTO alumnos(nombre,apellido,nota) VALUES (%s,%s,%s)'
#try:
#    cursor.execute(sql,("pedro","yllw",13))
#    connection.commit() # para confirmar en nuestra tabla
            # o sino no se vera en la tabla solo en la consola
#except Exception as e:
#    raise

def obtener_alumnos():
    #alumnosx = []
    with connection.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM alumnos")
            alumnosx = cursor.fetchall()
            return alumnosx
        except Exception as e:
            raise
    #connection.close()
    #return alumnosx

def insertar_alumno(nombre, apellido, nota):
    with connection.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO alumnos(nombre, apellido, nota) VALUES (%s, %s, %s)",(nombre, apellido, nota))
            connection.commit()
        except Exception as e:
            raise
    
    #connection.close()





#######-----Esto esta correcto , pero lo comento-----####
#sql='INSERT INTO alumnos(nombre,apellido,nota) VALUES (%s,%s,%s)'
#try:
#    cursor.execute(sql,("Pedro","Picapiedra",19))
#    connection.commit() # para confirmar en nuestra tabla
#            # o sino no se vera en la tabla solo en la consola
#except Exception as e:
#    raise


print(data)

app = Flask(__name__)
#app.secret_key= 'mysecretkey'
#
# 


@app.route('/')
def index():
   #return "Hello World"
   return render_template('indice.html')


@app.route("/agregar_alumno")
def formulario_agregar_alumno():
    return render_template("agregar_alumno.html")


#@app.route("/")
@app.route("/alumnos")
def alumnos():
    alumnos = obtener_alumnos()
    #return render_template("alumnos.html")
    return render_template("alumnos.html", alumnos=alumnos)


@app.route("/guardar_alumno", methods=["POST"])
def guardar_alumno():
    nombre = request.form["nombre"]
    apellido = request.form["apellido"]
    nota = request.form["nota"]
    insertar_alumno(nombre, apellido, nota)
    # De cualquier modo, y si todo fue bien, redireccionar
    return redirect("/alumnos")


#x=hello_world()
#print(x)

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)




