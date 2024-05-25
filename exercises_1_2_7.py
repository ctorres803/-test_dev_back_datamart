from concurrent.futures import ThreadPoolExecutor, as_completed
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
  result = "La mediana del conjunto es: " + str((median_left + median_right) / 2 )
  return result

def remove_duplicates(array_elems):
  # Se inicializa el array resultante
  resultado = []

  # Se recorren los elementos del array
  for num in array_elems:
    # Si el elemento no está en el array resultante, se añade
    if num not in resultado:
      resultado.append(num)

  return resultado


def busqueda_binaria(lista, objetivo, inicio, fin):
    # Caso base: si la parte de la lista no es válida
    if inicio > fin:
        return False
    
    # Encuentra el punto medio de la lista
    medio = (inicio + fin) // 2
    
    # Caso base: si el elemento medio es el objetivo
    if lista[medio] == objetivo:
        return True
    
    # Si el objetivo es menor que el elemento medio, buscar en la mitad izquierda
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, objetivo, inicio, medio - 1)
    
    # Si el objetivo es mayor que el elemento medio, buscar en la mitad derecha
    else:
        return busqueda_binaria(lista, objetivo, medio + 1, fin)

def mapeo_con_busqueda_binaria(lista1, lista2):
    resultados = []
    for elemento in lista2:
        encontrado = busqueda_binaria(lista1, elemento, 0, len(lista1) - 1)
        resultados.append(encontrado)
    return resultados

def mapeo_con_busqueda_binaria_paralelo(lista1, lista2, max_workers):
    def tarea_busqueda(elemento):
        return busqueda_binaria(lista1, elemento, 0, len(lista1) - 1)
    
    resultados = [False] * len(lista2)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futuros = {executor.submit(tarea_busqueda, elemento): idx for idx, elemento in enumerate(lista2)}
        
        for futuro in as_completed(futuros):
            idx = futuros[futuro]
            resultados[idx] = futuro.result()
    
    return resultados


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
  print("4. Busqueda binaria")
  print("5. Busqueda Binaria en parallel")
  print("6. Salir")
  print("---------------------------------")


  while True:
    try:
      opcion = int(input("Ingrese la opción deseada: "))
      if 1 <= opcion <= 6:
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
      random_list_1 = [random.randint(1, 100) for _ in range(opcion_1)]
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
      print("Función de busqueda binaria")
      opcion_1 = int(input("ingrese la dimension para el array: "))
      random_list_1 = [random.randint(1, 100) for _ in range(opcion_1)]
      random_list_1 = sorted(random_list_1)
      print("Random Array: ", random_list_1)
      opcion_2 = int(input("ingrese el número a buscar: "))
      start_time = time.time()
      print(busqueda_binaria(random_list_1, opcion_2, 0, len(random_list_1) - 1))
      end_time = time.time()
      print("Tiempo de ejecución busqueda_binaria: ", end_time - start_time)

    elif opcion_seleccionada == 5:
        print("Busqueda Binaria en paralelo")
        opcion_1 = int(input("ingrese la dimension para el array 1: "))
        random_list_1 = [random.randint(1, 100) for _ in range(opcion_1)]
        opcion_2 = int(input("ingrese la dimension para el array 2: "))
        random_list_2 = [random.randint(1, 100) for _ in range(opcion_2)]
        max_workers = 4  # Máximo número de threads
        start_time = time.time()
        resultados = mapeo_con_busqueda_binaria_paralelo(sorted(random_list_1), sorted(random_list_2), max_workers)
        end_time = time.time()
        print(f"Resultados de la búsqueda binaria en paralelo: {resultados}  con un timpo de ejecución de: {end_time - start_time}")


    elif opcion_seleccionada == 6:
        print("Saliendo del programa.")
        break


if __name__ == "__main__":
  main()





