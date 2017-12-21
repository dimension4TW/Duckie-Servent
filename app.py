from flask import Flask, render_template, request
from collections import deque

app = Flask(__name__)

state = "VEVLET"
location = "Leave Home"
environment = {
    "lightness": 0.0,
    "temperature":0.0,
    "humidity":0.0,
    "volume":0.0
}
aidMapping = {
    3:"Room A",
    4:"Room B"
}
previousLoc = "Y"
currentLoc = "Room A"
nextLoc = "Room A"
destLoc = "Room A"
currentPath = deque(["A","B","C"])

def mapLocation(aid):
    global aidMapping
    return aidMapping[aid]

def Dika(cur,des):
    return "X"

def updateState():
    global currentLoc, nextLoc, destLoc, previousLoc
    previousLoc = currentLoc
    currentLoc =  nextLoc
    nextLoc = Dika(currentLoc, destLoc) #if current == destination, next = current

def gardUpdateState():
    global currentLoc, nextLoc, destLoc, previousLoc
    previousLoc = currentLoc
    currentLoc =  nextLoc
    if(currentLoc == destLoc):
        if(currentLoc == "Room A"):
            destLoc = "Room B"
        print("You have arrived ",currentLoc, ". Now go to ",destLoc)
    nextLoc = Dika(currentLoc, destLoc)

def getNextMove(pre,cur,nxt):
    if(cur == "X"):
        if(pre == "Room A"):
            if(nxt == "Room B"):
                return "LEFT"
    else:
        return "STOP"

@app.route('/')
def dashboard():
    global state, destLoc, currentLoc
    return render_template('dashboard.html', state=state, destination = destLoc,location=currentLoc)

@app.route('/turn', methods=['GET'])
def turn():
    global nextLoc, previousLoc, state

    comeFrom = previousLoc
    if(state == "VELVET"):
        updateState()
    else:
        gardUpdateState()
    nextMove = getNextMove(comeFrom, currentLoc, nextLoc)
    print("Go ",nextMove,". Next Location: ",nextLoc)
    return nextMove

@app.route('/sendData', methods=['POST'])
def send_data():
    if request.method == 'POST':
        data = request.form['test']
        print(data)
        return data

@app.route('/getCurrentLoc', methods=['GET'])
def getCurrentLoc():
    global currentLoc
    #print(currentLoc)
    return currentLoc

@app.route('/getState', methods=['GET'])
def getState():
    print(state)
    return state

@app.route('/changeState', methods=['POST'])
def changeState():
    global state
    state = request.form['state']
    print(state)
    return state

@app.route('/changeDestination', methods=['POST'])
def changeDestination():
    global destLoc, currentLoc
    destLoc = request.form['location']
    state = "VELVET"
    #updateState()
    print("currentLoc: ",currentLoc, " destLoc: ",destLoc, "nextLoc: ",nextLoc)
    return render_template('dashboard.html', state=state, destination = destLoc,location=currentLoc)

@app.route('/display', methods=['GET'])
def getData():
    global environment
    print(environment)
    return render_template('display.html', environment = environment)
