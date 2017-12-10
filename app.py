from flask import Flask, render_template, request

app = Flask(__name__)

global state
state = "VEVLET"

@app.route('/')
def dashboard():
    global state
    return render_template('dashboard.html', state=state)

@app.route('/send_data', methods=['POST'])
def send_data():
    if request.method == 'POST':
        data = request.form['test']
        print(data)
        return data

@app.route('/get_location', methods=['GET'])
def get_locatoin():
    print(state)
    return state

@app.route('/change_state', methods=['POST'])
def change_state():
    global state
    state = request.form['state']
    print(state)
    return state
