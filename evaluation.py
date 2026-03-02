def evaluate():
    test_queries = [
        "Fresher software engineer with Python and DSA",
        "Data analyst with SQL experience"
    ]

    expected = [
        "Programming Skills - Python",
        "SQL Skills Test"
    ]

    correct = 0
    for q, exp in zip(test_queries, expected):
        if exp.lower() in q.lower():
            correct += 1

    accuracy = correct / len(test_queries)
    print("Evaluation Accuracy:", accuracy)

if __name__ == "__main__":
    evaluate()
