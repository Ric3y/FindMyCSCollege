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

    # Convert costs to integers
    try:
        min_cost = int(min_cost)
        max_cost = int(max_cost)
    except ValueError:
        return "Invalid input for cost. Please enter numeric values."

    # Get the student size range based on the size mapping
    min_students = size_mapping[size]["min"]
    max_students = size_mapping[size]["max"]

    # Call the get_colleges function with the user inputs
    colleges = get_colleges(state=state, costMin=min_cost, costMax=max_cost, sizeMin=min_students, sizeMax=max_students)

    college_info = ""
    for college in colleges:
        college_name = college['school.name']
        # Call the getAvgCompSciRating function with the college name
        avg_rating = getAvgCompSciRating(college_name)
        avg_rating_str = f"{avg_rating:.2f}" if avg_rating is not 0.0 else "N/A"

        college_info += f"""
            <p>
                <strong>Name:</strong> {college_name}<br>
                <strong>City:</strong> {college['school.city']}<br>
                <strong>State:</strong> {college['school.state']}<br>
                <strong>Student Size:</strong> {college['latest.student.size']}<br>
                <strong>Cost of Attendance:</strong> ${college['latest.cost.tuition.in_state']}<br>
                <strong>Avg Computer Science Professor Rating:</strong> {avg_rating_str}<br>
            </p>
        """   

    # Display a message using the collected inputs
    return f"""
        <link rel="stylesheet" href="/static/styles.css">
        <h1>College Information</h1>
        <form>
        <h4>State: {state}</h4>
        <h4>College Size: {size.capitalize()} (Student Range: {min_students} - {max_students} students)</h4>
        <h4>Cost of Attendance Range: ${min_cost} - ${max_cost}</h4>
        <h2>Colleges Found:</h2>
        {college_info if college_info else "<p>No colleges found.</p>"}
        </form>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
