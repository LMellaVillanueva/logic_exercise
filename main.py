"""
Dado un array de números y un número goal, encuentra los dos primeros números del array que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

from os import system
if system("clear") != 0: system("cls")

def find_first_sum(nums, goal):
  for i in range(len(nums) - 1):
    if nums[i] + nums[i + 1] == goal:
      return [i, i + 1]
  return None

  #! List comprehension que alcanza el resultado, pero retorna TODOS los índices con coincidencia
  # indexes = [[x, (x + 1)] for x in range(len(nums) - 1) if nums[x] + nums[x + 1] == goal]
  # return indexes if indexes else None


nums = [4, 5, 6, 2]
goal = 8

print(find_first_sum(nums, goal))