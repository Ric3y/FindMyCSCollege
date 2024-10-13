import json
from RateMyProfessorAPI_136.ratemyprofessor.__init__ import get_school_by_name
from ratemyprof_api.ratemyprof_api.ratemyprof_api import RateMyProfApi

# Load cache from a JSON file
def load_cache(filename='cache.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# Save cache to a JSON file
def save_cache(cache, filename='cache.json'):
    with open(filename, 'w') as f:
        json.dump(cache, f)

# Initialize cache
avg_rating_cache = load_cache()

def getListOfCompSciProfs(school):
    allCsProfs = []
    professors = school.professors  
    for professor_id, professor in professors.items():
        if "Computer Science" in professor.tDept or "computer science" in professor.tDept:
            allCsProfs.append(professor)
    return allCsProfs

def getAvgCompSciRating(school_name):
    # Check if the result is already cached
    if school_name in avg_rating_cache:
        return avg_rating_cache[school_name]

    school = get_school_by_name(school_name)
    total = -1
    if school is not None:  
        total = 0
        otherschool = RateMyProfApi(school.id)
        csProfs = getListOfCompSciProfs(otherschool)
        for prof in csProfs:
            total += prof.overall_rating
        average = total / len(csProfs)
    else:
        print("Invalid school name")
        average = None

    # Store the computed average in the cache
    avg_rating_cache[school_name] = average
    save_cache(avg_rating_cache)  # Save cache to file
    return average

# Example usage
print(getAvgCompSciRating("University of Texas at Austin")) # Should return cached result
