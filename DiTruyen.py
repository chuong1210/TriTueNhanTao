import random

# def fitness_function(individual):
#     """
#     Hàm đánh giá độ phù hợp của một cá thể.
#     Trong ví dụ này, chúng ta muốn tìm số nguyên dương nhỏ nhất sao cho tổng các số từ 1 đến n lớn hơn 100.
#     """
#     n = int("".join(map(str, individual)), 2)  # Chuyển đổi chuỗi bit thành số nguyên
#     total = n * (n + 1) // 2  # Sử dụng công thức tính tổng các số tự nhiên
#     if total > 100:
#         return total  # Trả về tổng nếu thỏa mãn điều kiện
#     else:
#         return 0  # Trả về 0 nếu không thỏa mãn điều kiện
def fitness_function(individual):
    n = int("".join(map(str, individual)), 2)
    total = n * (n + 1) // 2
    if total > 100:
        return 1 / (n + 1)  # Trả về giá trị giảm dần khi n tăng
    else:
        return 0

def crossover(parent1, parent2):
    """
    Toán tử chéo. Trong ví dụ này, chéo đơn giản.
    """
    crossover_point = random.randint(0, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

def mutation(individual, mutation_rate):
    """
    Toán tử đột biến. Đột biến ngẫu nhiên một bit với xác suất mutation_rate.
    """
    mutated_individual = []
    for bit in individual:
        if random.random() < mutation_rate:
            mutated_individual.append(1 - bit)  # Đột biến bit
        else:
            mutated_individual.append(bit)
    return mutated_individual

def genetic_algorithm(population_size, chromosome_length, generations, mutation_rate):
    """
    Giải thuật di truyền.
    """
    population = []
    for _ in range(population_size):
        individual = [random.randint(0, 1) for _ in range(chromosome_length)]
        population.append(individual)

    for generation in range(generations):
        new_population = []
        fitness_values = [(fitness_function(individual), individual) for individual in population]
        sorted_fitness = sorted(fitness_values, reverse=True)

        # Chọn lọc dựa trên xếp hạng. Chọn top 50%
        selected_individuals = sorted_fitness[:int(population_size * 0.5)] 
        
        # Thêm những cá thể tốt nhất vào thế hệ mới, giúp bảo tồn những giá trị tốt
        new_population.extend([individual for _, individual in selected_individuals])
        
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(selected_individuals, 2)
            child1, child2 = crossover(parent1[1], parent2[1])
            child1 = mutation(child1, mutation_rate)
            child2 = mutation(child2, mutation_rate)
            new_population.append(child1)
            new_population.append(child2)

        population = new_population

    # Tìm cá thể tốt nhất
    best_individual = max(population, key=lambda individual: fitness_function(individual))
    best_solution = int("".join(map(str, best_individual)), 2)
    return best_solution


# Ví dụ sử dụng
population_size = 100
chromosome_length = 10  # Số bit để biểu diễn số n
generations = 100
mutation_rate = 0.01

best_solution = genetic_algorithm(population_size, chromosome_length, generations, mutation_rate)

if best_solution > 0:
    print(f"Giải pháp tối ưu tìm được: {best_solution}")
else:
    print("Không tìm thấy giải pháp thỏa mãn.")