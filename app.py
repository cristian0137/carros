from flask import Flask, request, jsonify, render_template
from config.database import db, app
from models.Model_carro import Carro

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/Agregarcarro',methods = ['POST'])
def Agregar_carro():
    data = request.get_json()
    nuevo_carro = Carro(
        modelo = data.get('modelo'),
        color = data.get('color'),
        puertas = data.get('puertas')
    )
    db.session.add(nuevo_carro)
    db.session.commit()
    return 'Carro agregado', 200

@app.route('/Obtenercarros', methods = ['GET'])
def Obtener_carro():
    carros = Carro.query.all()
    carros_dict = [carro.to_dict() for carro in carros]
    return jsonify(carros_dict)

@app.route('/Eliminarcarro',methods=['DELETE'])
def Eliminarcarro():
    id = request.json['id']
    carro = Carro.query.get(id)
    
    if carro is None:
        return 'carro no encoontrado', 404
    db.session.delete(carro)
    db.session.commit()
    return 'Carro eliminado',200



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
