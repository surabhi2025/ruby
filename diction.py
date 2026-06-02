student_data = {
    "id1": {"name": "Keya", "class": "v", "subject": "english, math, science"},
    "1d2": {"name": "Yashni", "class": "v", "subject": "science, math"},
    "1d3": {"name": "Surabhi", "class": "v", "subject": "english, math, science,"},
    "1d4": {"name": "Tingting", "class": "v", "subject": "english, math, science"},}

result = {}
seen = set()

for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject"])
    if unique_key not in seen:
        seen.add(unique_key)
        result[student_id] = details

for k,v in result.items():
    print(k, ":", v)