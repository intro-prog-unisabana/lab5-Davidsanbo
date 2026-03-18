# Función para calcular el total de pasos
def total_steps(steps):
    return sum(steps)

# Función para calcular el promedio diario (entero)
def average_steps(steps):
    return sum(steps) // len(steps)

# Función para encontrar el máximo de pasos
def max_steps(steps):
    return max(steps)

# Función para encontrar el mínimo de pasos
def min_steps(steps):
    return min(steps)

# Función para verificar si se alcanzó la meta de 10000 pasos cada día
def goal_met(steps):
    results = []
    for s in steps:
        results.append(s >= 10000)
    return results
# Pedir pasos al usuario
user_input = input("Enter steps for 7 days separated by spaces:\n")

# Convertir a enteros
steps = list(map(int, user_input.split()))

# Calcular resultados
total = total_steps(steps)
average = average_steps(steps)
highest = max_steps(steps)
lowest = min_steps(steps)
goals = goal_met(steps)

# Imprimir resumen
print(f"Total steps: {total}")
print(f"Average daily steps: {average}")
print(f"Highest steps in a day: {highest}")
print(f"Lowest steps in a day: {lowest}")
print(f"Goal met each day: {goals}")