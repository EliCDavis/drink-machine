from flask import Flask, request, send_from_directory
app = Flask(__name__, static_url_path='')

from drink import Drink 
from drinkmachine import DrinkMachine 

flow_rate_oz_second = 0.0391
pump_one_pin = 18
pump_two_pin = 23

our_drink_machine = DrinkMachine(pump_one_pin, pump_two_pin, flow_rate_oz_second) 

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
    
    
print('starting server!')
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.run(host='0.0.0.0', debug=True)
