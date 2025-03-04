import random

def get_probability_input(prompt, default):
    """
    Solicita al usuario una probabilidad y la valida.
    Si el usuario no ingresa un valor, se usa el valor por defecto.
    """
    while True:
        try:
            value = input(f"{prompt} (valor entre 0 y 1, por defecto {default}): ")
            if value == "":  # Si el usuario no ingresa nada, se usa el valor por defecto
                return default
            value = float(value)  # Convertir la entrada a número flotante
            if 0 <= value <= 1:  # Verificar que esté en el rango válido
                return value
            else:
                print("⚠️ Error: Ingresa un valor entre 0 y 1.")
        except ValueError:
            print("⚠️ Error: Ingresa un número válido.")

# Solicitar probabilidades al usuario con valores por defecto
p_A = get_probability_input("Probabilidad de estar preparado", 0.6)  # Probabilidad de estar preparado
p_B = get_probability_input("Probabilidad de estar nervioso", 0.3)  # Probabilidad de estar nervioso
p_C_A1_B0 = get_probability_input("Probabilidad de aprobar si está preparado y no nervioso", 0.9)
p_C_A1_B1 = get_probability_input("Probabilidad de aprobar si está preparado y nervioso", 0.7)
p_C_A0_B0 = get_probability_input("Probabilidad de aprobar si NO está preparado y no nervioso", 0.8)
p_C_A0_B1 = get_probability_input("Probabilidad de aprobar si NO está preparado y nervioso", 0.4)

def probability_preparation():
    """Determina si el estudiante está preparado con base en la probabilidad ingresada."""
    return 1 if random.random() < p_A else 0  # Genera 1 si está preparado, 0 si no

def probability_nervous():
    """Determina si el estudiante está nervioso con base en la probabilidad ingresada."""
    return 1 if random.random() < p_B else 0  # Genera 1 si está nervioso, 0 si no

def probability_pass(a, b):
    """
    Determina la probabilidad de aprobar con base en la preparación (A) y los nervios (B).
    Recibe:
        a: 1 si está preparado, 0 si no.
        b: 1 si está nervioso, 0 si no.
    Devuelve:
        Probabilidad de aprobar el examen.
    """
    if a == 1 and b == 0:
        return p_C_A1_B0  # Preparado y no nervioso
    elif a == 1 and b == 1:
        return p_C_A1_B1  # Preparado y nervioso
    elif a == 0 and b == 0:
        return p_C_A0_B0  # No preparado y no nervioso
    elif a == 0 and b == 1:
        return p_C_A0_B1  # No preparado y nervioso

def simulate_exam():
    """
    Simula un examen para un estudiante.
    1. Determina si el estudiante está preparado.
    2. Determina si el estudiante está nervioso.
    3. Calcula la probabilidad de aprobar.
    4. Decide si aprueba o no en función de esa probabilidad.
    Devuelve:
        1 si aprueba, 0 si no.
    """
    a = probability_preparation()  # Obtener si el estudiante está preparado
    b = probability_nervous()  # Obtener si el estudiante está nervioso
    pass_probability = probability_pass(a, b)  # Obtener la probabilidad de aprobar
    return 1 if random.random() < pass_probability else 0  # Decide si aprueba o no

# Número de simulaciones a realizar
num_trials = 1000  # Se realizarán 1000 pruebas
results = [simulate_exam() for _ in range(num_trials)]  # Ejecutar simulaciones y guardar resultados

# Calcular la tasa de aprobación
pass_rate = sum(results) / num_trials  # Promedio de aprobados
print(f"Tasa de aprobación en {num_trials} simulaciones: {pass_rate:.2f}")  # Mostrar resultado
