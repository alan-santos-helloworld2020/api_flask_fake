from flask import Flask,request
from flask.json import jsonify
from functools import wraps
import jwt
import datetime
app = Flask(__name__)


app.config['SECRET_KEY'] = '123456789'
dados = []

def check_token(func):
    @wraps(func)
    def wrapped(*args,**kwargs):
        token = request.headers['Authorization'].split(" ")[1]
        if not token:
            return jsonify({'auth':False,'token':False}),403

        try:
            data = jwt.decode(token,app.config['SECRET_KEY'],algorithms="HS256")
            print(data)
        except:
            return jsonify({'auth' : False,'erro':'Token Invalido!'}), 403
        return func(*args,**kwargs)
    return wrapped

##******************************************************************************
@app.route('/login',methods=['POST'])
def login():
    if request.json['username'] == 'admin' and request.json['password'] == '123':
        token = jwt.encode({'username':request.json['username'],
        'exp':datetime.datetime.utcnow() + datetime.timedelta(seconds=60)
        },app.config['SECRET_KEY'],algorithm="HS256")
        return jsonify({'auth':True,'token':token})
    else:
        return jsonify({'auth':False,'token':False})

@app.route('/',methods=['GET'])
@check_token
def index():
        return jsonify(dados)

@app.route('/<id>',methods=['GET'])
@check_token
def pesquisar(id):
    i = len(dados)
    if i > 0:
        return jsonify(dados[int(id)])
    else:
        return jsonify({'msg':False})

@app.route('/',methods=['POST'])
@check_token
def salvar():
    user = request.get_json()
    dados.append(user)
    return jsonify({'msg':True,'user':user})

@app.route('/<id>',methods=['PUT'])
@check_token
def editar(id):
    user = request.get_json()
    dados[int(id)] = user
    return jsonify({'msg':True,'user':user})

@app.route('/<id>',methods=['DELETE'])
@check_token
def deletar(id):
    dados.pop(int(id))
    return jsonify({'msg':True})




    
  




        