from flask import Flask,request
from flask.json import jsonify
app = Flask(__name__)

dados = []

@app.route('/',methods=['GET'])
def index():
    return jsonify(dados)

@app.route('/<id>',methods=['GET'])
def pesquisar(id):
    i = len(dados)
    if i > 0:
        return jsonify(dados[int(id)])
    else:
        return jsonify({'msg':False})

@app.route('/',methods=['POST'])
def salvar():
    user = request.get_json()
    dados.append(user)
    return jsonify({'msg':True,'user':user})

@app.route('/<id>',methods=['PUT'])
def editar(id):
    user = request.get_json()
    dados[int(id)] = user
    return jsonify({'msg':True,'user':user})

@app.route('/<id>',methods=['DELETE'])
def deletar(id):
    dados.pop(int(id))
    return jsonify({'msg':True})




    
  




        