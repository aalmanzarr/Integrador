from flask import Flask, jsonify, request, render_template, send_file
from flask_cors import CORS
from matplotlib import pyplot as plt
import datetime
import random


app = Flask(__name__)
CORS(app)

now=datetime.datetime.now()
tipo_medicion = {'sensor':'HC-SR04', 'variable':'DISTANCIA', 'unidades':'Cm'}
mediciones=[
        {'fecha':datetime.datetime.strftime(now,'%Y-%m-%d %H:%M:%S'), **tipo_medicion, 'valor':random.randint(2,450),'ID':1},
        {'fecha':"2019-08-21 27:45:00", **tipo_medicion, 'valor':random.randint(2,450),'ID':2},
        {'fecha':datetime.datetime.strftime(now,'%Y-%m-%d %H:%M:%S'), **tipo_medicion, 'valor':random.randint(2,450),'ID':3},
        {'fecha':"2019-08-21 27:45:00", **tipo_medicion, 'valor':random.randint(2,450),'ID':4},
        {'fecha':datetime.datetime.strftime(now,'%Y-%m-%d %H:%M:%S'), **tipo_medicion, 'valor':random.randint(2,450),'ID':5},
        {'fecha':"2019-08-21 27:45:00", **tipo_medicion, 'valor':random.randint(2,450),'ID':6},
        {'fecha':datetime.datetime.strftime(now,'%Y-%m-%d %H:%M:%S'), **tipo_medicion, 'valor':random.randint(2,450),'ID':7},
        {'fecha':"2019-08-21 27:45:00", **tipo_medicion, 'valor':random.randint(2,450),'ID':8},
]

def getMedia():          
        media=[]
        for t in range(len(mediciones)):
                media.append(mediciones[t].get('valor'))
        media = sum(media)/float(len(mediciones))  
        return media

@app.route('/mediciones')
def getAll():
        return jsonify(mediciones)

@app.route('/mediciones/grafica')
def Graficador():
        media=getMedia()
        prom=[]
        y=[]
        z=[]
        for x in range(len(mediciones)):
                y.append(mediciones[x].get('ID'))
                z.append(mediciones[x].get('valor'))
        for u in range(len(mediciones)*2):  
                prom.append(media)
        plt.plot(y,z,prom) 
        plt.savefig("Distancia.png")
        filename = 'Distancia.png'
        return send_file(filename, mimetype='Distancia.png') 


if __name__ == "__main__":
    app.run(debug=True,
            port=5000)
                        
