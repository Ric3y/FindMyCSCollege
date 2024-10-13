from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_state', methods=['POST'])
def submit_state():
    state = request.form['state']
    size = request.form['size']
    min_cost = request.form['minCost']  # Get minimum cost from the form
    max_cost = request.form['maxCost']  # Get maximum cost from the form

    # Display a message using the collected inputs
    return f"""
        <h1>College Information</h1>
        <p>State: {state}</p>
        <p>College Size: {size} students</p>
        <p>Cost of Attendance Range: ${min_cost} - ${max_cost}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
