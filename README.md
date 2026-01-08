# Global Education Nested Data Engineering (Capstone)

## 📌 Overview
This capstone project demonstrates mastery of deeply nested dictionary structures
using pure Python. It focuses on data cleaning, structural cleanup, flattening,
and analytical aggregation — preparing for Pandas and Data Science workflows.

## 🧠 Concepts Covered
- Deep hierarchical traversal
- Safe deletion patterns (collect → delete)
- Structural cleanup (inside → outside)
- Data uncoupling (flattening)
- Feature engineering
- Aggregation and analytics

## 🌍 Dataset Structure
The dataset models a global education system:

- Continents
  - Countries
    - Universities
      - Faculties
        - Departments
          - Students (scores)

Messy real-world cases such as missing values and invalid scores are intentionally included.

## ⚙️ Project Workflow
1. Clean invalid student records
2. Remove empty structural containers
3. Flatten nested data into analytic rows
4. Compute country-level averages
5. Identify best-performing department globally

## ▶️ How to Run
```bash
python global_education_nested_data_capstone.py

🎯 Learning Outcome
- Completing this project demonstrates readiness for:
- Pandas DataFrames
- GroupBy operations
- Real-world data preprocessing
- Data engineering pipelines

✍️ Author

Udeme Ebere
