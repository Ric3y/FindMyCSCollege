from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_state', methods=['POST'])
def submit_state():
    state = request.form['state']
    city = request.form['city']
    size = request.form['size']
    cost = request.form['cost']

    # Display a message using the collected inputs
    return f"""
        <h1>College Information</h1>
        <p>State: {state}</p>
        <p>City: {city}</p>
        <p>College Size: {size} students</p>
        <p>Cost of Attendance: ${cost}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
