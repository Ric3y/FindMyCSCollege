import requests

def get_colleges(state=None, name=None, costMin=None, costMax=None, sizeMin=None, sizeMax=None):
    base_url = "https://api.data.gov/ed/collegescorecard/v1/schools.json"
    params = {
        'api_key': 'OQ2eq2aL7mZdZURogCcjKWxKXWzjFLw8bkJgh49Z',  # Replace with your API key,
        'fields': 'id,school,latest,cost',  # Include necessary fields
        'per_page': 100,
    }
    # Add state parameter if provided
    if state:
        params['school.state'] = state.upper()  # Ensure state code is uppercase
    if name:
        params['school.name'] = name
    if costMin is not None and costMax is not None:
        params['latest.cost.tuition.in_state__range'] = f"{costMin}..{costMax}"  # Using range syntax
    if sizeMin is not None and sizeMax is not None:
        params['latest.student.size__range'] = f"{sizeMin}..{sizeMax}"  # Using range syntax
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        print(f"Error: {response.status_code} - {response.json()}")
        return []

# Example usage  # Change this to a specific state code if needed
colleges = get_colleges('TX', '', 0, 10000, 0, 10000)
for college in colleges:
    if (college['latest.academics.program.bachelors.computer'] == 1):
        print(
            f"Name: {college['school.name']}, "
            f"City: {college['school.city']}, "
            f"State: {college['school.state']}, "
            f"Student Size: {college['latest.student.size']}, "
            f"Student Cost: ${college['latest.cost.tuition.in_state']}, ",
            f"{college['latest.academics.program.bachelors.computer']}"
    )
