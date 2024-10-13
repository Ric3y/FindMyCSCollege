from programs.RateMyProfessorAPI_136.ratemyprofessor.__init__ import get_school_by_name
from .ratemyprof_api.ratemyprof_api.ratemyprof_api import RateMyProfApi
def getListOfCompSciProfs(school):
    allCsProfs = []
    professors = school.professors  
    for professor_id, professor in professors.items():
        if "Computer Science" in professor.tDept or "computer science" in professor.tDept:
            allCsProfs.append(professor)
    return allCsProfs

def getAvgCompSciRating(school_name):
    school = get_school_by_name(school_name)
    total = -1
    if school is not None:  
        total = 0
        otherschool = RateMyProfApi(school.id)
        csProfs = getListOfCompSciProfs(otherschool)
        for prof in csProfs:
            total += prof.overall_rating
    else:
        print("invalid school name")
    return total/len(csProfs)
print(getAvgCompSciRating("University Of Texas at Arlington"))