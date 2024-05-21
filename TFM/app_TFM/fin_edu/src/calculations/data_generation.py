import numpy as np
import pandas as pd

np.random.seed(42)

def generate_synthetic_data(n_schools, n_students_per_school):
    total_students = n_schools * n_students_per_school

    schools = np.repeat(np.arange(1, n_schools + 1), n_students_per_school)
    ages = np.random.randint(6, 12, total_students)
    genders = np.random.choice(['M', 'F'], total_students)
    socioeconomic_status = np.random.randint(1, 4, total_students)
    attendance = np.random.uniform(75, 100, total_students)
    extracurricular_participation = np.random.randint(0, 2, total_students)
    final_grades = np.random.uniform(50, 100, total_students)

    latitudes = np.random.uniform(-3.0, 3.0, n_schools)
    longitudes = np.random.uniform(-3.0, 3.0, n_schools)

    data = pd.DataFrame({
        'school': schools,
        'age': ages,
        'gender': genders,
        'socioeconomic_status': socioeconomic_status,
        'attendance': attendance,
        'extracurricular_participation': extracurricular_participation,
        'final_grade': final_grades
    })

    school_locations = pd.DataFrame({
        'school': np.arange(1, n_schools + 1),
        'latitude': latitudes,
        'longitude': longitudes
    })

    return data, school_locations
