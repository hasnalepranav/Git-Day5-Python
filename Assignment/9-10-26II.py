students = {
    101: {"Name": "Aditi", "Scores": [20, 20, 25]},
    102: {"Name": "Rahul", "Scores": [45, 60, 50]},
    103: {"Name": "Sneha", "Scores": [0,  14, 95]},
    104: {"Name": "Karan", "Scores": [55, 12, 43]},
    105: {"Name": "Priya", "Scores": [49, 51, 47, 33]},
}

for sid details in students.items():
    avg = sum(details["Scores"]) / len(details["Scores"])
    

