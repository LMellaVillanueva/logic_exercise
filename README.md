First Sum Exercise

Busca el primer par de números adyacentes que sean igual a un número dado 'goal'.

Objetivo

Este ejercicio forma parte de mi práctica para mis estudios de Python y mejorar mi lógica de desarrollador. La función find_first_sum(nums, goal) recorre una lista de números enteros y retorna los índices de los primeros números que sumados dan de resultado 'goal'.

Ejemplo de uso:

def find_first_sum(nums, goal):
    for i in range(len(nums) - 1):
        if nums[i] + nums[i + 1] == goal:
            return [i, i + 1]
    return None


nums = [4, 5, 6, 2]
goal = 8

print(find_first_sum(nums, goal))  # Resultado: [0, 1]


Cómo ejecutar el script

1. Clonar este repositorio:
    git clone https://github.com/LMellaVillanueva/logic_exercise.git

2. Navegar al directorio:
    cd main.py

3. Ejecutar el archivo:
    python main.py

Apuntes de implementación

- Se usa enfoque iterativo para asegurar eficiencia y claridad.
- Intento de implementar List Comprehension, pero devolvía todas las coincidencias, retornando todos los índices en vez de los primeros.