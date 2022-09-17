from flask import Flask, request, jsonify, render_template

app = Flask(__name__)
app._static_folder = 'templates'

@app.route("/")
def hello_world():
    return render_template('index.html', message="This is a Flask App containerised with Docker")


@app.route('/data', methods=['POST'])
def data():
    testData = request.json
    return jsonify(testData)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
