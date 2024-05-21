def calculate_ranking(data):
    ranking_criteria = ['attendance', 'socioeconomic_status', 'extracurricular_participation', 'final_grade']
    weights = [0.3, 0.2, 0.2, 0.3]  # Asignar pesos a cada criterio

    data['rank_score'] = (data[ranking_criteria] * weights).sum(axis=1)
    school_ranking = data.groupby('school')['rank_score'].mean().sort_values(ascending=False)
    return school_ranking

def allocate_budget(school_ranking, total_budget):
    budget_allocation = school_ranking / school_ranking.sum() * total_budget
    return budget_allocation
