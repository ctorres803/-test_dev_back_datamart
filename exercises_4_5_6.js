//* Ejercicio 4
function isAnagram(str1, str2) {
  // Si las cadenas tienen diferente longitud, no son anagramas
  if (str1.length !== str2.length) {
    return false;
  }

  // Convertir las cadenas a minúsculas y eliminar espacios
  str1 = str1.toLowerCase().replace(/ /g, '');
  str2 = str2.toLowerCase().replace(/ /g, '');

  // Convertir las cadenas en arreglos y ordenarlos alfabéticamente
  const arr1 = str1.split('');
  arr1.sort();
  const arr2 = str2.split('');
  arr2.sort();

  // Comparar los arreglos ordenados
  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] !== arr2[i]) {
      return false;
    }
  }

  // Si se llega a este punto, las cadenas son anagramas
  return true;
}

//*modificar las cadenas para probar la funcion
const str1 = "elvis";
const str2 = "visel";

if (isAnagram(str1, str2)) {
  console.log(`\nisAnagram: ${str1} y ${str2} son anagramas \n`);
} else {
  console.log(`${str1} y ${str2} no son anagramas \n`);
}

//* Ejercicio 5
function findCommonElements(listOfLists) {
  // Si la lista de listas está vacía, retorna una lista vacía
  if (listOfLists.length === 0) {
    return [];
  }

  // Inicializar una lista para almacenar los elementos comunes
  const commonElements = [];

  // Obtener el primer elemento de la lista de listas
  const firstList = listOfLists[0];

  // Recorrer cada elemento de la primera lista
  for (const element of firstList) {
    // Suponer que el elemento es común
    let isCommon = true;

    // Recorrer las demás listas
    for (const otherList of listOfLists.slice(1)) {
      // Si el elemento no está presente en la otra lista, no es común
      if (!otherList.includes(element)) {
        isCommon = false;
        break;
      }
    }

    // Si el elemento es común, agregarlo a la lista de elementos comunes
    if (isCommon) {
      commonElements.push(element);
    }
  }

  // Retornar la lista de elementos comunes
  return commonElements;
}

//* Modificar la lista de listas para probar la funcion
const listOfLists = [
  [1, 2, 3],
  [1, 3, 4],
  [3, 4, 1],
];

const commonElements = findCommonElements(listOfLists);
console.log(`findCommonElements - detecto elemento(s) comun(es): ${commonElements}\n`)

//* Ejercicio 6

// Ordena recursivamente un arreglo
function mergeSort(array) {
  if (array.length <= 1) {
    return array;
  }
  // Divide el arreglo en dos mitades usando slice
  const middle = Math.floor(array.length / 2);
  const left = array.slice(0, middle);
  const right = array.slice(middle);  

  return merge(mergeSort(left), mergeSort(right));
}

// Combina subArreglos
function merge(left, right) {
  const result = [];
  let i = 0;
  let j = 0;

  while (i < left.length && j < right.length) {
    if (left[i] < right[j]) {
      result.push(left[i]);
      i++;
    } else {
      result.push(right[j]);
      j++;
    }
  }

  return [...result, ...left.slice(i), ...right.slice(j)];
}

// usar mergesoft para ordenar el arreglo
console.log(`mergeSort - ordena el arreglo: ${mergeSort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])}\n`);