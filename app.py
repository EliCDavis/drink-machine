from flask import Flask, request, send_from_directory
app = Flask(__name__, static_url_path='')

from drink import Drink 
from drinkmachine import DrinkMachine 

our_drink_machine = DrinkMachine() 

@app.route("/")
def hello():
    return app.send_static_file('index.html')

@app.route("/drink", methods=('GET', 'POST'))
def get_drink_request():

    if request.method == 'POST':
        return our_drink_machine.make_drink(Drink(request.json["pumpOne"], request.json["pumpTwo"]))
    elif request.method == 'GET':
        return our_drink_machine.current_drink_progress() 

    return "error occured"