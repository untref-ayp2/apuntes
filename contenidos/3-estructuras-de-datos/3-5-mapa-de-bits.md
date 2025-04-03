---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Mapas de Bits

Los mapas de bits son estructuras de datos que permiten registrar la presencia o ausencia de un conjunto de elementos. Cada posición del mapa del bit representa un elemento, y el valor de cada posición indica si el elemento está presente (1) o ausente (0). 

Una de las implementaciones más eficientes de mapas de bits es el uso de números enteros, aprovechando su representación binaria. Cada bits de un número entero puede representar la presencia o ausencia de un elemento. Por ejemplo, si tenemos un conjunto de elementos que van del 0 al 31, podemos usar un número entero de 32 bits para representar la presencia o ausencia de cada elemento. Esta implementación es eficiente en términos de espacio y tiempo, ya que permite realizar operaciones de búsqueda, inserción y eliminación en tiempo constante $O(1)$.

Los mapas de bits se utilizan en diversas aplicaciones, como la representación de conjuntos, la compresión de datos y la implementación de algoritmos de búsqueda. Son especialmente útiles en situaciones donde se requiere un acceso rápido a los elementos y se tiene un conjunto limitado de posibles valores.

```{figure} ../assets/images/MapaDeBitsQuorum.svg
---
width: 500px
name: quorum
---
Quorum en una sesión del Congreso.
```

## Implementación con números enteros

Supongamos que tenemos un conjunto de elementos que van del 0 al 31. Podemos usar un número entero de 32 bits para representar la presencia o ausencia de cada elemento. Por ejemplo, si el número entero es 15, cuya representación en binario con 32 bits es `00000000000000000000000000001111`, esto indica que los elementos 0, 1, 2 y 3 están presentes, mientras que los demás elementos están ausentes. El bit menos significativo (a la derecha) representa el elemento 0, el siguiente bit representa el elemento 1, y así sucesivamente.

### Operaciones sobre bits

Los mapas de bits permiten realizar diversas operaciones sobre los bits, como la inserción, eliminación y búsqueda de elementos. Estas operaciones se pueden implementar utilizando operadores binarios que implementan las operaciones lógicas booleanas. 

Las operaciones lógicas booleanas son:

_AND_  (Producto Lógico)
: Operación que devuelve 1 si ambos bits son 1, y 0 en caso contrario. El operador _AND_ se representa con el símbolo `&`.

_OR_ (Suma Lógica)
: Operación que devuelve 1 si al menos uno de los bits es 1, y 0 en caso contrario. El operador _OR_ se representa con el símbolo `|`.

_XOR_ (OR Exclusivo)
: Operación que devuelve 1 si los bits son diferentes (uno es 1 y el otro es 0), y 0 en caso contrario. El operador _XOR_ se representa con el símbolo `^`.

_NOT_ (Negación)
: Operación que invierte el valor de un bit (0 se convierte en 1 y 1 se convierte en 0). El operador _NOT_ se representa con el símbolo `^`.

A continuación se presenta la tabla de verdad de las operaciones lógicas booleanas sobre bits:

:::{table} Tabla de verdad de las operaciones sobre bits
:align: center

| A | B | `(A & B)`| `(A \| B)` | `(A ^ B)` | `(^A)` |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 0 | 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 1 | 1 | 1 |
| 1 | 0 | 0 | 1 | 1 | 0 |
| 1 | 1 | 1 | 1 | 0 | 0 |

:::

### Operadores binarios en Go

Go soporta 6 operaciones binarias y una operación unaria que se pueden utilizar para manipular los bits de un número entero. Estas operaciones son:

_AND_
: El operador _AND_ (`&`) compara dos números bit a bit y devuelve un nuevo número donde cada bit es 1 si ambos bits de entrada son 1, y 0 en caso contrario. Por ejemplo:

```go
a := 0b1100 // 12
b := 0b1010 // 10
c := a & b // 0b1000 (8)
```

Esto significa que el resultado `c` tiene un 1 en la posición 3 (de derecha a izquierda) porque tanto `a` como `b` tienen un 1 en esa posición.

_OR_
: El operador _OR_ (`|`) compara dos números bit a bit y devuelve un nuevo número donde cada bit es 1 si al menos uno de los bits de entrada es 1. Por ejemplo:

```go
a := 0b1100 // 12
b := 0b1010 // 10
c := a | b // 0b1110 (14)
```
Esto significa que el resultado `c` tiene un 1 en las posiciones 1, 2 y 3 porque al menos uno de los bits de entrada es 1 en esas posiciones.

_XOR_
: El operador _OR Exclusivo_, _XOR_ (`^`) compara dos números bit a bit y devuelve un nuevo número donde cada bit es 1 si los bits de entrada son diferentes (uno es 1 y el otro es 0). Por ejemplo:

```go
a := 0b1100 // 12
b := 0b1010 // 10
c := a ^ b // 0b0110 (6)
```

Esto significa que el resultado `c` tiene un 1 en las posiciones 1 y 2 porque los bits de entrada son diferentes en esas posiciones.

Desplazamiento a Izquierda o _Left Shift_
: El operador de desplazamiento a la izquierda (`<<`) desplaza todos los bits de un número hacia la izquierda, llenando los bits vacíos con ceros. Por ejemplo:

```go
a := 0b0001 // 1
b := a << 2 // 0b0100 (4)
```
Esto significa que el resultado `b` tiene un 1 en la posición 2 porque se ha desplazado el bit 1, originalmente en la posición 0, dos posiciones a la izquierda.

Desplazamiento a Derecha o _Right Shift_
: El operador de desplazamiento a la derecha (`>>`) desplaza todos los bits de un número hacia la derecha, llenando los bits vacíos con ceros. Por ejemplo:

```go
a := 0b1000 // 8
b := a >> 2 // 0b0010 (2)
```
Esto significa que el resultado `b` tiene un 1 en la posición 1 porque se ha desplazado el bit 1, originalmente en la posición 3, dos posiciones a la derecha.


_NOT_
: La única operación unaria es la negación o complemento (los 0 se cambian por 1 y viceversa). Esta operación se representa con el símbolo `^`. Por ejemplo:

```go
a := 0b1100 // 12
b := ^a // 0b0011 (3)
```
Esto significa que el resultado `b` tiene 1 en las posiciones 0 y 1 y 0 en las posiciones 2 y 3 complementariamente a la entrada.


_AND NOT_ o _bit clear_
: El operador _bit clear_ (`&^`) es una combinación de los operadores _AND_ y _NOT_. Este operador se utiliza para borrar bits específicos en un número. Es como realizar la operación AND entre el primer operando y el complemento del segundo. Por ejemplo:

```go 
a := 0b1100 
b := 0b1010 // El complemento de b es 0b0101 (5)
c := a &^ b // 0b1100 & 0b0101 = 0b0100 (4)
```
Esto significa que el resultado `c` tiene un 1 en la posición 2 porque se han borrado los bits 1 y 3 de la entrada `a`.

:::{table} Operaciones sobre bits en Go
:align: center
:width: 50%

| Operación | Símbolo | Ejemplo |
| :---: | :---: | :---: |
| AND | `&` | `a & b` |
| OR | `\|` | `a | b` |
| XOR | `^` | `a ^ b` |
| Desplazamiento a Izquierda | `<<` | `a << 2` |
| Desplazamiento a Derecha | `>>` | `a >> 2` |
| NOT | `^` | `^a` |
| AND NOT | `&^` | `a &^ b` |

:::

Go también soporta los operadores de asignación compuesta, que combinan una operación binaria con una asignación. Estos operadores son:

:::{table} Operadores de asignación compuesta en Go
:align: center
:width: 50%

| Símbolo | Operación | Ejemplo | 
| :---: | :---: | :---: |
| `&=` | `a = a & b` | `a &= b` |
| `\|=` | `a = a \| b` | `a \|= b` |
| `^=` | `a = a ^ b` | `a ^= b` |
| `<<=` | `a = a << b` | `a <<= b` |
| `>>=` | `a = a >> b` | `a >>= b` |
| `&^=` | `a = a &^ b` | `a &^= b` |
:::

## Ejercicios

1- Implementar un TAD denominado BitMap que permita representar un conjunto de elementos sobre enteros de 32 bits. El TAD debe permitir las siguientes operaciones:

- `NewBitMap()`: Crea un nuevo mapa de bits vacío.
- `On(pos uint8)`: Activa el bit en la posición `pos` del mapa de bits.
- `Off(pos uint8)`: Desactiva el bit en la posición `pos` del mapa de bits.
- `IsOn(pos uint8)`: Devuelve `true` si el bit en la posición `pos` está activo, y `false` en caso contrario.
- `IsOff(pos uint8)`: Devuelve `true` si el bit en la posición `pos` está inactivo, y `false` en caso contrario.
- `CountOn()`: Devuelve la cantidad de bits activos en el mapa de bits.
- `String()`: Devuelve una representación en cadena del mapa de bits.