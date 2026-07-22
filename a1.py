student_data = {
    "id1": {"name": "HARSHH", "class":"V", "subject_intergration": "english, maths, science, soc.sci" },

     "id2": {"name": "SONAL", "class":"IV", "subject_intergration": "english, maths, science, soc.sci, art" },

      "id3": {"name": "HARSHH", "class":"V", "subject_intergration": "english, maths, science, soc.sci" },

       "id4": {"name": "RAHUL", "class":"IX", "subject_intergration": "english, maths, science, soc.sci, hindi" },
}
result = {}
seen_keys = []
for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject_intergration"])

    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details

for k, v in result.items():
    print(k, ":", v)