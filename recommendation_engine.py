def recommend_assessments(candidate, assessments):
    recommendations = []

    for test in assessments:
        score = 0
        reasons = []

        if candidate["role"] in test["roles"]:
            score += 2
            reasons.append("role match")

        for skill in candidate["skills"]:
            if skill in test["skills"]:
                score += 2
                reasons.append(f"skill match: {skill}")

        if test["level"] == "All" or test["level"] == candidate["experience"]:
            score += 1
            reasons.append("experience level match")

        if score >= 3:
            recommendations.append({
                "assessment": test["name"],
                "score": score,
                "reasons": reasons
            })

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

for item in result:
    print(f"{item['assessment']} (Score: {item['score']})")
    print("Reasons:", ", ".join(item["reasons"]))
    print()
