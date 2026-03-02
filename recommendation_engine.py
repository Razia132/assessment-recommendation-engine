import json

def recommend_assessments(candidate, assessments):
    recommendations = []

    for test in assessments:
        score = 0

        if candidate["role"] in test["roles"]:
            score += 2

        for skill in candidate["skills"]:
            if skill in test["skills"]:
                score += 2

        if test["level"] == "All" or test["level"] == candidate["experience"]:
            score += 1

        if score >= 3:
            recommendations.append(test["name"])

    return recommendations


if __name__ == "__main__":
    with open("assessments.json") as f:
        assessments = json.load(f)

    candidate = {
        "role": "Software Engineer",
        "experience": "Fresher",
        "skills": ["Python", "DSA", "SQL"],
        "industry": "IT"
    }

    result = recommend_assessments(candidate, assessments)
    print("Recommended Assessments:", result)
