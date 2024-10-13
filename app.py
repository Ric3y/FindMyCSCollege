from flask import Flask, render_template, request
from programs.CollegeInformationFunctions import get_colleges  
from programs.GetUniversityCompSciProfAvg import getAvgCompSciRating

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
    # Collecting user input from the form
    state = request.form['state']
    size = request.form['size']
    min_cost = request.form['minCost']  # Get minimum cost from the form
    max_cost = request.form['maxCost']  # Get maximum cost from the form

    min_students = size_mapping[size]["min"]
    max_students = size_mapping[size]["max"]

    # Call the get_colleges function with the user inputs
    colleges = get_colleges(state=state, costMin=min_cost, costMax=max_cost, sizeMin=size, sizeMax=size)

    college_info = ""
    for college in colleges:
        college_info += f"""
            <p>
                <strong>Name:</strong> {college['school.name']}<br>
                <strong>City:</strong> {college['school.city']}<br>
                <strong>State:</strong> {college['school.state']}<br>
                <strong>Student Size:</strong> {college['latest.student.size']}<br>
                <strong>Cost of Attendance:</strong> ${college['latest.cost.tuition.in_state']}<br>
            </p>
        """   

    # Display a message using the collected inputs
    return f"""
        <h1>College Information</h1>
        <p>State: {state}</p>
        <p>College Size: {size.capitalize()} (Student Range: {min_students} - {max_students} students) </p>
        <p>Cost of Attendance Range: ${min_cost} - ${max_cost}</p>
        <h2>Colleges Found:</h2>
        {college_info if college_info else "<p>No colleges found.</p>"}
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
