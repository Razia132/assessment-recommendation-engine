# Assessment Recommendation Engine

## Problem Statement
Hiring organizations like SHL offer a wide range of assessments. Selecting the right assessment for a candidate based on their role, skills, and experience is crucial for accurate evaluation.

This project implements a simple **Assessment Recommendation Engine** that recommends suitable assessments from an SHL-style product catalogue using a rule-based scoring approach.

---

## Approach
The solution uses a **rule-based recommendation system**:

- Candidate details such as role, skills, and experience are taken as input
- Each assessment is evaluated against the candidate profile
- Scores are assigned based on:
  - Role match
  - Skill match
  - Experience level match
- Assessments crossing a defined score threshold are recommended

This approach ensures **transparency, explainability, and simplicity**, which are important in real-world assessment systems.

---

## Assessment Catalogue
The assessment catalogue is stored in `assessments.json` and contains:
- Assessment name
- Applicable roles
- Required skills
- Experience level

This mimics a simplified SHL product catalogue.

---

## How the Recommendation Works
Scoring Logic:
- +2 points if candidate role matches assessment role
- +2 points for each matching skill
- +1 point if experience level matches
- Assessments with score ≥ 3 are recommended

---

## Project Structure
assessment-recommendation-engine/
├── recommendation_engine.py
├── assessments.json
├── requirements.txt
├── README.md

---

## How to Run
1. Clone the repository
2. Navigate to the project directory
3. Run the command:
python recommendation_engine.py

---

## Output
The program prints the list of recommended assessments for a sample candidate profile along with the reasoning.

---

## Assumptions
- Candidate profile is provided in a structured format
- Assessment catalogue is static and predefined
- Rule-based logic is sufficient for demonstration purposes

---

## Future Enhancements
- Add a REST API using Flask
- Integrate machine learning-based ranking
- Support real-time candidate input
- Expand assessment catalogue
