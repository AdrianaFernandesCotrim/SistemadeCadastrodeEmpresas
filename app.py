import os

from flask import (Flask, current_app, jsonify, redirect, render_template)
from flask import request
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from requisicao import consulta_cnpj
import db
from db import empresas

Session = sessionmaker(bind=db.engine)
session = Session()


project_dir = 'mysql+pymysql://u221579840_inf_warehouse:Inf_warehouse123@sql775.main-hosting.eu/u221579840_inf_warehouse'
database_file = project_dir


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = database_file
db = SQLAlchemy(app)
@app.cli.command

@app.route('/empresas', methods =['GET'])
def mostrar():
    session.rollback()
    enterprises = session.query(empresas).all()
    # print(enterprises)
    return render_template('resultados.html',result=enterprises)

@app.route('/cadastro', methods=['GET', 'POST'])
def home():
    #metodo para cadastras novas empresas
    if request.form:
        cnpj=request.form.get('cnpj')
        resultado = consulta_cnpj(cnpj)
        new_enterprise = empresas(cnpj, resultado[0],resultado[1],resultado[2],resultado[3],resultado[4], resultado[5], resultado[6],resultado[7],resultado[8])
        db.session.add(new_enterprise)
        db.session.commit()
    return render_template('home.html')
@app.route('/atualizar', methods=['GET','POST'])
def att():
    session.rollback()
    if request.form:
        cnpj = request.form.get("cnpj")
        nome = request.form.get("nome")
        logradouro = request.form.get("logradouro")
        numero = request.form.get("numero")
        bairro = request.form.get("bairro")
        municipio = request.form.get('municipio')
        uf = request.form.get('uf')
        cep = request.form.get('cep')
        telefone = request.form.get('telefone')
        email = request.form.get('email')
        enterprise =  session.query(empresas).get(cnpj)
        enterprise.cnpj = cnpj
        enterprise.Nome = nome
        enterprise.Logradouro = logradouro 
        enterprise.Numero = numero 
        enterprise.Bairro = bairro
        enterprise.Municipio = municipio
        enterprise.UF = uf
        enterprise.CEP = cep
        enterprise.TELEFONE = telefone
        enterprise.EMAIL = email
        session.commit()
    return render_template('atualizar.html')
@app.route('/deletar', methods=['GET','POST'])
def deletar():
    session.rollback()
    if request.form:
        cod = request.form.get("cod")
        enterprise =  session.query(empresas).filter(empresas.cnpj==cod).delete()
        print(session.query(empresas).filter(empresas.cnpj==cod))
        session.commit()
    enterprises = session.query(empresas).all()
    return render_template('deletar.html', result=enterprises)

if __name__ == '__main__':
    app.run(debug=True)