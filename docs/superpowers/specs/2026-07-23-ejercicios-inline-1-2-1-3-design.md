# Especificación: Ejercicios inline para capítulos 1-2 y 1-3

## Problema

Los capítulos `1-2-memoria.md` y `1-3-analisis-de-algoritmos.md` referencian
ejercicios en rutas de `taller-go` que nunca existieron:

- `1-2-memoria.md`: `taller-go/02-memoria/ejercicios/`
- `1-3-analisis-de-algoritmos.md`: `taller-go/03-analisis-de-algoritmos/ejercicios/`

Ninguno de esos directorios existe en `taller-go` ni en ningún otro lugar del
monorepo, ni hay registro en git history de que hayan existido.

Además, estos capítulos son conceptuales (no de programación), por lo que sus
ejercicios son de lápiz y papel, no requieren código compilable.

## Solución

Reemplazar la referencia externa por ejercicios inline en lista numerada simple
dentro de cada archivo `.md`, bajo la sección `## Ejercicios`.

## Archivos a modificar

| Archivo | Cambio |
|---|---|
| `apuntes/contenidos/1-presentacion/1-2-memoria.md` | Reemplazar sección Ejercicios con 5 ejercicios inline |
| `apuntes/contenidos/1-presentacion/1-3-analisis-de-algoritmos.md` | Reemplazar sección Ejercicios con 4 ejercicios inline (el 4.º con 7 fragmentos) |

## Ejercicios: 1-2 Memoria

Cinco ejercicios de lápiz y papel sobre gestión de memoria en Go:

1. **Mapa de memoria.** Dado un código Go con variables globales (`var` a nivel
   paquete), locales y punteros, dibujar el mapa de memoria indicando qué va al
   segmento de datos, stack y heap.

2. **Escape analysis.** Dadas 3-4 funciones cortas, identificar qué variables
   escapan al heap y justificar por qué el compilador decide eso.

3. **Strings en heap.** Explicar por qué los strings en Go siempre almacenan su
   contenido en el heap, incluso cuando la variable es local.

4. **Stack frames.** Dada una secuencia de llamadas A→B→C con parámetros y
   variables locales, describir el contenido del stack en cada paso.

5. **GC concurrente.** Explicar cómo el garbage collector de Go evita memory
   leaks, qué significa *stop-the-world* y por qué las pausas son mínimas.

## Ejercicios: 1-3 Análisis de Algoritmos

Cuatro ejercicios adaptados de la guía de ejercicios 6 (fuente original en Java,
convertida a pseudocódigo del apunte). Los ejercicios 1, 2, 3 y 7 de esa guía.

1. **Máximo (O(1)).** Pseudocódigo con FUNCION/SI/ENTONCES/SINO. Calcular
   operaciones elementales y determinar O grande.

2. **Potencia (O(n)).** Pseudocódigo con FUNCION/PARA. Calcular OE, determinar
   O grande.

3. **Recorrer arreglo (O(n)).** Pseudocódigo con FUNCION/MIENTRAS. Calcular OE,
   determinar O grande.

4. **Fragmentos de ciclos (ej. 7).** Siete fragmentos en pseudocódigo, calcular
   O grande de cada uno:
   - F1: `PARA i←0 HASTA n-1` → O(n)
   - F2: `PARA i←0 HASTA n-1 PASO 2` → O(n/2) = O(n)
   - F3: dos PARA anidados hasta n → O(n²)
   - F4: dos PARA sucesivos hasta n → O(n) + O(n) = O(n)
   - F5: PARA i hasta n, PARA j hasta n² → O(n³)
   - F6: PARA i hasta n, PARA j hasta i → O(n²)
   - F7: tres PARA: i→n, j→n², k→j → O(n⁵)

## Formato

Lista numerada simple de Markdown. Cada ejercicio en un párrafo o bloque corto
con `{code-block} text` para pseudocódigo cuando sea necesario.

## No tocar

- `ESTILOS.md`: no se modifica. La excepción para capítulos conceptuales es
  puntual y no requiere cambiar la guía general.
- Otros capítulos: no se modifican. Solo 1-2 y 1-3.
- `taller-go`: no se crean directorios nuevos.
