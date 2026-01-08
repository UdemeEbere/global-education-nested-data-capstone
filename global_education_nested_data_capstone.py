"""
Project: Global Education Nested Data Engineering (Capstone)
Author: Udeme Ebere

This capstone project demonstrates mastery of deeply nested dictionary structures
using pure Python. It covers data cleaning, structural cleanup, data uncoupling
(flattening), and analytical aggregation — preparing for Pandas and Data Science.

Skills demonstrated:
- Deep hierarchical traversal
- Safe deletion patterns (collect → delete)
- Structural cleanup (inside → outside)
- Feature engineering
- Aggregation and analytics
"""

# ============================================================
# DATASET
# ============================================================

system = {
    "continents": {
        "Africa": {
            "countries": {
                "Nigeria": {
                    "universities": {
                        "UniLagos": {
                            "faculties": {
                                "Science": {
                                    "departments": {
                                        "Math": {
                                            "students": {
                                                1: {"name": "Ada", "scores": {"calc": 85, "algebra": 78}},
                                                2: {"name": None, "scores": {"calc": 90, "algebra": 88}},
                                                3: {"name": "Tunde", "scores": {"calc": -10, "algebra": 65}},
                                            }
                                        },
                                        "Physics": {
                                            "students": {
                                                4: {"name": "Bola", "scores": {"calc": 92, "algebra": None}},
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "Europe": {
            "countries": {
                "Germany": {
                    "universities": {
                        "UniBerlin": {
                            "faculties": {
                                "Engineering": {
                                    "departments": {
                                        "CS": {
                                            "students": {
                                                1: {"name": "Hans", "scores": {"calc": 88, "algebra": 90}},
                                                5: {"name": "Lena", "scores": {"calc": 95, "algebra": 93}},
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

# ============================================================
# PART A — DATA CLEANING
# ============================================================

continents = system["continents"]

for continent_data in continents.values():
    for country_data in continent_data["countries"].values():
        for university_data in country_data["universities"].values():
            for faculty_data in university_data["faculties"].values():
                for department_data in faculty_data["departments"].values():

                    students_to_delete = set()

                    for stu_id, stu_info in department_data["students"].items():
                        name = stu_info["name"]
                        calc = stu_info["scores"]["calc"]
                        algebra = stu_info["scores"]["algebra"]

                        if name is None:
                            students_to_delete.add(stu_id)
                            continue

                        if calc is None or calc < 0 or calc > 100:
                            students_to_delete.add(stu_id)
                            continue

                        if algebra is None or algebra < 0 or algebra > 100:
                            students_to_delete.add(stu_id)

                    for stu_id in students_to_delete:
                        del department_data["students"][stu_id]

# ============================================================
# PART B — STRUCTURAL CLEANUP (INSIDE → OUTSIDE)
# ============================================================

# Remove empty departments
for continent_data in continents.values():
    for country_data in continent_data["countries"].values():
        for university_data in country_data["universities"].values():
            for faculty_data in university_data["faculties"].values():

                departments_to_delete = set()

                for dept_name, dept_data in faculty_data["departments"].items():
                    if not dept_data["students"]:
                        departments_to_delete.add(dept_name)

                for dept_name in departments_to_delete:
                    del faculty_data["departments"][dept_name]

# Remove empty faculties
for continent_data in continents.values():
    for country_data in continent_data["countries"].values():
        for university_data in country_data["universities"].values():

            faculties_to_delete = set()

            for fac_name, fac_data in university_data["faculties"].items():
                if not fac_data["departments"]:
                    faculties_to_delete.add(fac_name)

            for fac_name in faculties_to_delete:
                del university_data["faculties"][fac_name]

# Remove empty universities
for continent_data in continents.values():
    for country_data in continent_data["countries"].values():

        universities_to_delete = set()

        for uni_name, uni_data in country_data["universities"].items():
            if not uni_data["faculties"]:
                universities_to_delete.add(uni_name)

        for uni_name in universities_to_delete:
            del country_data["universities"][uni_name]

# Remove empty countries
for continent_data in continents.values():

    countries_to_delete = set()

    for country_name, country_data in continent_data["countries"].items():
        if not country_data["universities"]:
            countries_to_delete.add(country_name)

    for country_name in countries_to_delete:
        del continent_data["countries"][country_name]

# Remove empty continents
continents_to_delete = set()

for continent_name, continent_data in continents.items():
    if not continent_data["countries"]:
        continents_to_delete.add(continent_name)

for continent_name in continents_to_delete:
    del continents[continent_name]

# ============================================================
# PART C — DATA UNCOUPLING (FLATTENING)
# ============================================================

rows = []

for continent, continent_data in continents.items():
    for country, country_data in continent_data["countries"].items():
        for university, university_data in country_data["universities"].items():
            for faculty, faculty_data in university_data["faculties"].items():
                for department, department_data in faculty_data["departments"].items():
                    for student_id, student in department_data["students"].items():

                        calc = student["scores"]["calc"]
                        algebra = student["scores"]["algebra"]
                        avg_score = (calc + algebra) / 2

                        rows.append(
                            (
                                continent,
                                country,
                                university,
                                faculty,
                                department,
                                student_id,
                                student["name"],
                                calc,
                                algebra,
                                avg_score
                            )
                        )

# ============================================================
# PART D1 — AVERAGE SCORE PER COUNTRY
# ============================================================

score_by_country = {}

for row in rows:
    country = row[1]
    avg_score = row[9]

    if country not in score_by_country:
        score_by_country[country] = []

    score_by_country[country].append(avg_score)

average_score_by_country = {
    country: sum(scores) / len(scores)
    for country, scores in score_by_country.items()
}

# ============================================================
# PART D2 — BEST PERFORMING DEPARTMENT
# ============================================================

score_by_department = {}

for row in rows:
    department = row[4]
    avg_score = row[9]

    if department not in score_by_department:
        score_by_department[department] = []

    score_by_department[department].append(avg_score)

avg_score_by_department = {
    dept: sum(scores) / len(scores)
    for dept, scores in score_by_department.items()
}

best_department = max(
    avg_score_by_department,
    key=avg_score_by_department.get
)

# ============================================================
# PART E — FINAL OUTPUT
# ============================================================

print("\n--- FINAL ANALYTICS REPORT ---")
print("Average Score by Country:", average_score_by_country)
print(
    f"Best Performing Department: {best_department} | "
    f"Average Score: {avg_score_by_department[best_department]}"
)
print("Total Students Processed:", len(rows))
print("Nested dictionary mastery completed. Ready for Pandas.")
