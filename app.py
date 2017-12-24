from flask import Flask, render_template, request
from collections import deque

app = Flask(__name__)

state = "VELVET"
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
action = "STOP"
#currentPath = deque(["A","B","C"])

def mapLocation(aid):
    global aidMapping
    return aidMapping[aid]

def getNextLoc(cur,dest):
    if(cur == dest):
        return cur
    elif(cur == "Room A"):
        if(dest == "Room B"):
            return "X"
        if(dest == "Room C"):
            return "X"
    elif(cur == "X"):
        if(dest == "Room B"):
            return "Room B"
        elif(dest == "Room C"):
            return "Room C"

def update():
    global currentLoc, nextLoc, destLoc, previousLoc
    if(currentLoc != destLoc):
        previousLoc = currentLoc
        currentLoc =  nextLoc

def gardUpdate():
    global currentLoc, nextLoc, destLoc, previousLoc
    previousLoc = currentLoc
    currentLoc =  nextLoc
    if(currentLoc == destLoc):
        if(currentLoc == "Room A"):
            destLoc = "Room B"
        print("You have arrived ",currentLoc, ". Now go to ",destLoc)

def getNextMove(pre,cur,nxt,dest):
    if(cur == dest):
        return "STOP"
    elif(cur =="Room A"):
        if(pre == "Y"):
            if(nxt == "X"):
                return "STRAIGHT"
    elif(cur == "X"):
        if(pre == "Room A"):
            if(nxt == "Room B"):
                return "LEFT"
            elif(nxt == "Room C"):
                return "RIGHT"
    else:
        return "STOP"

@app.route('/')
def dashboard():
    global state, destLoc, currentLoc
    return render_template('dashboard.html', state=state, destination = destLoc,location=currentLoc)

@app.route('/turn', methods=['GET'])
def turn():
    global currentLoc, destLoc, nextLoc, previousLoc, state, action
    #comeFrom = previousLoc
    if(state == "VELVET"):
        if(action != "STOP"):
            update()
    else:
        gardUpdate()
    nextLoc = getNextLoc(currentLoc, destLoc)
    action = getNextMove(previousLoc, currentLoc, nextLoc, destLoc)
    print("From ",previousLoc," Action:",action," Current Location:",currentLoc," Next Location:",nextLoc)
    return action

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
    print("currentLoc: ",currentLoc, " destLoc: ",destLoc)
    return render_template('dashboard.html', state=state, destination = destLoc,location=currentLoc)

@app.route('/display', methods=['GET'])
def getData():
    global environment
    print(environment)
    return render_template('display.html', environment = environment)
