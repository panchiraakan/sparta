from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from pokeapi import retrieve_pokemons

app = Flask(__name__)

client = MongoClient('mongodb+srv://basket19250:<password>@cluster0.8wbmfzp.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/SpartaChatbot", methods=["POST"])
def SpartaChatbot_post():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']

    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive
    }

@app.route("/pokemons", methods=["GET"])
def getpokemons():

    pokemons = retrieve_pokemons()
    return jsonify(pokemons)