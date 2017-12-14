from flask import Flask, render_template, request

app = Flask(__name__)

global state
state = "VEVLET"
location = "Leave Home"
environment = {
    "lightness": 0.0,
    "temperature":0.0,
    "humidity":0.0,
    "volume":0.0
}

@app.route('/')
def dashboard():
    global state
    return render_template('dashboard.html', state=state, location=location)

@app.route('/sendData', methods=['POST'])
def send_data():
    if request.method == 'POST':
        data = request.form['test']
        print(data)
        return data

@app.route('/getState', methods=['GET'])
def getLocatoin():
    print(state)
    return state

@app.route('/changeState', methods=['POST'])
def changeState():
    global state
    state = request.form['state']
    print(state)
    return state

@app.route('/changeLocation', methods=['POST'])
def changeLocation():
    global location
    location = request.form['location']
    state = "VELVET"
    print(location)
    return render_template('dashboard.html', state=state, location=location)

@app.route('/display', methods=['GET'])
def getData():
    global environment
    print(environment)
    return render_template('display.html', environment = environment)
