def process_scores(scores):
    avg = sum(scores) / len(scores)
    print("Average:", avg)
    print("Highest:", max(scores))
    print("Lowest:", min(scores))
scores = [85, 92, 78, 90, 88]
process_scores(scores)
