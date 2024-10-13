from flask import Flask, render_template, request

app = Flask(__name__)

size_mapping = {
    "small": {"min": 0, "max": 5000},
    "medium": {"min": 5000, "max": 15000},
    "large": {"min": 15000, "max": 100000}  # Setting a large max for large universities
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_state', methods=['POST'])
def submit_state():
    state = request.form['state']
    city = request.form['city']
    size = request.form['size']
    min_cost = request.form['minCost']  # Get minimum cost from the form
    max_cost = request.form['maxCost']  # Get maximum cost from the form

    min_students = size_mapping[size]["min"]
    max_students = size_mapping[size]["max"]

    # Display a message using the collected inputs
    return f"""
        <h1>College Information</h1>
        <p>State: {state}</p>
        <p>City: {city}</p>
        <p>College Size: {size.capitalize()} (Student Range: {min_students} - {max_students} students) </p>
        <p>Cost of Attendance Range: ${min_cost} - ${max_cost}</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
