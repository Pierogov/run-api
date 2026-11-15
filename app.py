from flask import Flask, jsonify

app = Flask(__name__)
timesPath = "./times/"

@app.route('/api/run/5', methods=['GET'])
def time5():
    completion, content = handleFile(timesPath + "5.txt")
    return jsonify({"distance": 5000, "time": content, "completed" : completion})

@app.route('/api/run/10', methods=['GET'])
def time10():
    completion, content = handleFile(timesPath + "10.txt")
    return jsonify({"distance": 10000, "time": content, "completed" : completion})

@app.route('/api/run/21', methods=['GET'])
def time21():
    completion, content = handleFile(timesPath + "21.txt")
    return jsonify({"distance": 21097.5, "time": content, "completed" : completion})

@app.route('/api/run/42', methods=['GET'])
def time42():
    completion, content = handleFile(timesPath + "42.txt")
    return jsonify({"distance": 42195, "time": content, "completed" : completion})

def handleFile(filePath):
    try: 
        file = open(filePath, "r+")
        content = file.read().strip()
        file.close()
        completion = True
        if content == "":
            completion = False
    except FileNotFoundError:
        file = open(filePath, "x")
        completion = False
        content = ""
        file.close()
    return completion, content
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)