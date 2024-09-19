# Оцінювання претендентів за різними критеріями
applicants = [
    [3, 7, 2, 9],
    [8, 3, 6, 7],
    [4, 8, 3, 5],
    [9, 6, 5, 4]
]

# Коефіцієнти важливості критеріїв
criteria_weights = [8, 9, 6, 7]

# Розрахунок сукупних балів для кожного претендента
applicants_total_scores = []
for applicant in applicants:
    total = 0
    for i in range(len(applicant)):
        total += applicant[i] * criteria_weights[i]
    applicants_total_scores.append(total)

applicant_names = ['A1', 'A2', 'A3', 'A4']

# Визначення претендента з найвищим балом
highest_score = max(applicants_total_scores)
best_applicant_index = applicants_total_scores.index(highest_score)
top_applicant = applicant_names[best_applicant_index]

print(f"Кращий претендент: {top_applicant}")
print(f"Найвищий бал: {highest_score}")
