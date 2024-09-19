# Оцінка продуктивності юристів за показниками
lawyers = [
    [85, 30, 22, 0.65, 6],
    [60, 20, 10, 0.6, 7],
    [30, 12, 5, 0.45, 5],
    [75, 24, 13, 0.7, 8],
    [40, 15, 7, 0.55, 7]
]

# Вагові значення для кожного параметра
criteria_weights = [7, 5, 6, 8, 6]

# Функція для пошуку мінімуму та максимуму по кожному критерію
def find_min_max(data):
    transposed_data = list(map(list, zip(*data)))
    mins = [min(column) for column in transposed_data]
    maxs = [max(column) for column in transposed_data]
    return mins, maxs

# Нормалізація даних
def normalize_data(dataset, min_vals, max_vals):
    normalized_data = []
    for entry in dataset:
        norm_entry = []
        for idx, value in enumerate(entry):
            if max_vals[idx] == min_vals[idx]:
                norm_entry.append(0)  
            else:
                norm_entry.append((value - min_vals[idx]) / (max_vals[idx] - min_vals[idx]))
        normalized_data.append(norm_entry)
    return normalized_data

# Спеціальна нормалізація для другого критерію
def normalize_second_criterion(normalized_dataset, original_dataset, max_vals, min_vals):
    for i in range(len(normalized_dataset)):
        normalized_dataset[i][1] = (max_vals[1] - original_dataset[i][1]) / (max_vals[1] - min_vals[1])
    return normalized_dataset

# Обчислення загальних балів
def calculate_scores(normalized_data, weights):
    scores = []
    for entry in normalized_data:
        total_score = sum([entry[i] * weights[i] for i in range(len(weights))])
        scores.append(total_score)
    return scores

# Імена юристів
names = ['A1', 'A2', 'A3', 'A4', 'A5']

# Основна логіка
min_values, max_values = find_min_max(lawyers)
normalized_lawyers = normalize_data(lawyers, min_values, max_values)
normalized_lawyers = normalize_second_criterion(normalized_lawyers, lawyers, max_values, min_values)
scores = calculate_scores(normalized_lawyers, criteria_weights)

# Визначення юриста з найвищим балом
best_index = scores.index(max(scores))
print(f"Найкращий адвокат: {names[best_index]}")
print(f"Підсумковий бал: {scores[best_index]}")
