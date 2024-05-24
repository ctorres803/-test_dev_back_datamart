import random
import time

def merge_arrays(array1, array2):
  # Se inicializa el array resultante
  resultado = []

  # Se recorren ambos arrays simultáneamente
  i = 0
  j = 0
  while i < len(array1) and j < len(array2):
    if array1[i] < array2[j]:
      resultado.append(array1[i])
      i += 1
    else:
      resultado.append(array2[j])
      j += 1

  # Se añaden los elementos restantes del primer array si los hay
  resultado.extend(array1[i:])

  # Se añaden los elementos restantes del segundo array si los hay
  resultado.extend(array2[j:])

  return resultado


def find_median(array_nums):
  if not array_nums:
    return None

  # Ordena el array en orden ascendente
  sorted_array_nums = sorted(array_nums)

  # Calcula la longitud del array ordenado
  array_length = len(sorted_array_nums)

  # Si la longitud es impar, la mediana es el elemento central
  if array_length % 2 == 1:
    return sorted_array_nums[array_length // 2]

  # Si la longitud es par, la mediana es el promedio de los dos elementos centrales
  median_left = sorted_array_nums[(array_length - 1) // 2]
  median_right = sorted_array_nums[(array_length + 1) // 2]
  return (median_left + median_right) / 2

def remove_duplicates(array_elems):
  # Se inicializa el array resultante
  resultado = []

  # Se recorren los elementos del array
  for num in array_elems:
    # Si el elemento no está en el array resultante, se añade
    if num not in resultado:
      resultado.append(num)

  return resultado



def mostrar_menu():
  """
  Muestra un menú al usuario y le permite seleccionar una opción.

  Devuelve:
    La opción seleccionada por el usuario (un entero).
  """
  print("---------------------------------")
  print("Menú principal:")
  print("1. merge_arrays")
  print("2. find_median")
  print("3. remove_Sduplicates")
  print("4. Salir")
  print("---------------------------------")


  while True:
    try:
      opcion = int(input("Ingrese la opción deseada: "))
      if 1 <= opcion <= 4:
        return opcion
      else:
        # opcion = int(input("Ingrese la opción deseada: "))
        print("Opción inválida. Intente nuevamente.")
    except ValueError:
      print("Error: Debe ingresar un número entero.")

def main():
  """
  Función principal del programa.
  """
  while True:
    opcion_seleccionada = mostrar_menu()

    if opcion_seleccionada == 1:
      print("Función para funcionar arrays")
      opcion_1 = int(input("ingrese la dimension para el array 1: "))
      random_list_1 = [random.randint(1, 100) for _ in range(opcion_1)]
      opcion_2 = int(input("ingrese la dimension para el array 2: "))
      random_list_2 = [random.randint(1, 100) for _ in range(opcion_2)]
      start_time = time.time()
      print(merge_arrays(sorted(random_list_1), sorted(random_list_2)))
      end_time = time.time()
      print("Tiempo de ejecución merge_arrays: ", end_time - start_time)
    
    elif opcion_seleccionada == 2:
      print("Función para encontrar la mediana")
      opcion_1 = int(input("ingrese la dimension para el array: "))
      random_list_1 = [random.randint(1, 3) for _ in range(opcion_1)]
      print("Random Array: ", random_list_1)
      start_time = time.time()
      print(find_median(random_list_1))
      end_time = time.time()
      print("Tiempo de ejecución find_median: ", end_time - start_time)

    elif opcion_seleccionada == 3:
      opcion_1 = int(input("ingrese la dimension para el array: "))
      random_list_1 = [random.randint(1, 100) for _ in range(opcion_1)]
      start_time = time.time()
      print(remove_duplicates(random_list_1))
      end_time = time.time()
      print("Tiempo de ejecución remove_duplicates: ", end_time - start_time)

    elif opcion_seleccionada == 4:
        print("Saliendo del programa.")
        break

if __name__ == "__main__":
  main()





