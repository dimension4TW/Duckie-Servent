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

previousLoc = "Door"
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
            return "Z"
        if(dest == "Room C"):
            return "Z"
    elif(cur == "Z"):
        if(dest == "Room B"):
            return "Room B"

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
        if(pre == "Z" and nxt == "Door"):
            return "STRAIGHT"
        elif(pre == "Door" and nxt == "Z"):
            return "STRAIGHT"
        elif(pre == "Door" and nxt == "Door"):
            return "INVERSE"
        elif(pre == "Z" and nxt == "Z"):
            return "INVERSE"

    elif(cur =="Room B"):
        if(pre == "X" and nxt == "Z"):
            return "STRAIGHT"
        elif(pre == "Z" and nxt == "X"):
            return "STRAIGHT"
        elif(pre == "X" and nxt == "X"):
            return "INVERSE"
        elif(pre == "Z" and nxt == "Z"):
            return "INVERSE"

    elif(cur =="Room C"):
        if(pre == "X" and nxt == "D"):
            return "STRAIGHT"
        elif(pre == "D" and nxt == "X"):
            return "STRAIGHT"
        elif(pre == "X" and nxt == "X"):
            return "INVERSE"
        elif(pre == "D" and nxt == "D"):
            return "INVERSE"

    elif(cur == "Z"):
        if(pre == "Room A"):
            if(nxt == "Room B"):
                return "RIGHT"
            elif(nxt == "Y"):
                return "STRAIGHT"
            elif(nxt == "Room A"):
                return "INVERSE"
        elif(pre == "Room B"):
            if(nxt == "Room A"):
                return "LEFT"
            elif(nxt == "Room B"):
                return "INVERSE"
            elif(nxt == "Y"):
                return "RIGHT"
        elif(pre == "Y"):
            if(nxt == "Room A"):
                return "STRAIGHT"
            elif(nxt == "Room B"):
                return "LEFT"
            elif(nxt == "Y"):
                return "INVERSE"

    elif(cur == "X"):
        if(pre == "Room B"):
            if(nxt == "Room B"):
                return "INVERSE"
            elif(nxt == "Room C"):
                return "RIGHT"
            elif(nxt == "Y"):
                return "LEFT"
        elif(pre == "Room C"):
            if(nxt == "Room B"):
                return "LEFT"
            elif(nxt == "Room C"):
                return "INVERSE"
            elif(nxt == "Y"):
                return "STRAIGHT"
        elif(pre == "Y"):
            if(nxt == "Room B"):
                return "RIGHT"
            elif(nxt == "Room C"):
                return "STRAIGHT"
            elif(nxt == "Y"):
                return "INVERSE"

    elif(cur == "Y"):
        if(pre == "Door"):
            if(nxt == "Door"):
                return "INVERSE"
            elif(nxt == "X"):
                return "LEFT"
            elif(nxt == "Z"):
                return "STRAIGHT"
        elif(pre == "X"):
            if(nxt == "Door"):
                return "RIGHT"
            elif(nxt == "X"):
                return "INVERSE"
            elif(nxt == "Z"):
                return "STRAIGHT"
        elif(pre == "Z"):
            if(nxt == "Door"):
                return "LEFT"
            elif(nxt == "X"):
                return "STRAIGHT"
            elif(nxt == "Z"):
                return "INVERSE"

    elif(cur == "Door"):
        if(pre == "Room A"):
            if(nxt == "Room A"):
                return "INVERSE"
            elif(nxt == "Room C"):
                return "STRAIGHT"
            elif(nxt == "Y"):
                return "STRAIGHT"
        elif(pre == "Room C"):
            if(nxt == "Room A"):
                return "STRAIGHT"
            elif(nxt == "Room C"):
                return "INVERSE"
            elif(nxt == "Y"):
                return "LEFT"
        elif(pre == "Y"):
            if(nxt == "Room A"):
                return "LEFT"
            elif(nxt == "Room C"):
                return "RIGHT"
            elif(nxt == "Y"):
                return "INVERSE"
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
