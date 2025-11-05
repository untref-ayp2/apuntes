---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# Algoritmos Ávidos

Los algoritmos ávidos o _greedy_ en inglés, son algoritmos diseñados generalmente para resolver problemas de optimización. Los algoritmos que resuelven este tipo de problemas generalmente lo hacen en etapas, realizando, a cada paso, algunos cálculos hasta llegar al resultado buscado. Un algoritmo ávido o codicioso siempre hace la elección que parece mejor en el momento. Es decir, hace una elección localmente óptima con la esperanza de que esta elección conduzca a una solución globalmente óptima. En otras palabras con los datos que está procesando en ese momento, toma la mejor decisión posible.

La estrategia ávida no siempre funciona, depende de la naturaleza del problema y de los datos, por lo que hay analizar bien el problema antes de seguir esta estrategia.

La principal ventaja de este tipo de algoritmos es que es muy fácil de implementar y entender.

Por ejemplo veamos a continuación un problema clásico:

```{card} Cambio de moneda
Un cajero automático tiene que ser capaz de entregar la cantidad de pesos que se le requiere utilizando la menor cantidad de billetes y monedas.

+++

**Optimización**: Entregar la mayor cantidad posible de los billetes de mayor denominación.
```

Por ejemplo, en Argentina, a Mayo de 2024 se emplean monedas de \$1, \$2, \$5 y \$10, y billetes de \$10, \$20, \$50, \$100, \$200, \$500, \$1.000, \$2.000 y \$10.000. Si el cajero tiene que entregar \$5.528

La solución será:

```{math}
2 \times $2000 + 1 \times $1000 + 1 \times $500 + 1 \times $20 + 1 \times $5 + 1 \times $2 +1 \times $1
```

En total se entregan 8 piezas.

````{prf:algorithm} Cambio de moneda
**Entrada**

- `billetes`: lista con las denominaciones disponibles ordenada de mayor a menor.
- `cantidad`: monto a cambiar

**Salida**

- `cambio` : diccionario cuyas claves son las denominaciones y cuyo valor son las cantidades a entregar de cada denominación

```{code-block}
---
linenos: true
---
PARA CADA denominacion EN billetes HACER
    SI cantidad >= denominacion ENTONCES
        cantidad_billetes := cantidad / denominacion
        cambio[denominacion] := cantidad_billetes
        cantidad := cantidad MOD denominacion
    FIN_SI
FIN_PARA
```

````

A partir de este fragmento nos podemos preguntar:

1. ¿Siempre puede entregar el cambio solicitado?

2. ¿Siempre entrega la menor cantidad de billetes?

Para que siempre pueda entregar el monto solicitado, es preciso contar con la moneda de \$1, para asegurarnos que podrá entregar cualquier monto.

Para asegurar que siempre da la menor cantidad de billetes, el sistema de denominaciones debe ser canónico. Es decir las denominaciones no pueden ser cualquiera, sino que deben ser un conjunto que asegure que siempre funciona el algoritmo ávido. Además deben estar ordenadas de mayor a menor.

Por ejemplo si las denominaciones fueran: \$1, \$2, \$5, \$10, \$20, \$50, \$100, \$200, \$500, \$800 y \$1.000 y tiene que dar \$2.400, nuestro algoritmo ávido daría 2 x \$1.000 + 2 x \$200 en lugar de dar 3 billetes de \$800.

La verificación formal de que un algoritmo ávido es correcto es un tema complejo y no siempre se puede hacer. En general se hace por inducción, es decir se prueba que la elección localmente óptima lleva a una solución globalmente óptima. Se puede hacer utilizando técnicas de programación dinámica.

A continuación otro ejemplo de algoritmo ávido muy popular en la literatura:

````{card} Plan de actividades
Se tiene un conjunto de actividades que se pueden realizar en un tiempo determinado. Cada actividad $a_i$ tiene un tiempo de inicio $s_i$ y un tiempo de finalización $f_i$. Se desea seleccionar la mayor cantidad de actividades que no se superpongan.

Dos actividades $a_i$ y $a_j$ son compatibles si los intervalos $[s_i, f_i)$ y $[s_j, f_j)$ no se superponen. Es decir:

```{math}
---
label: compatibilidad
---
f_i \leq s_j
```

O

```{math}
---
label: compatibilidad2
---
f_j \leq s_i
```

+++

**Optimización**: Elegir la actividad que **termina primero** entre las no elegidas, siempre y cuando sea compatible con las actividades ya elegidas.
````

Supongamos que tenemos las siguientes actividades, ordenadas por tiempo de finalización:

```{figure} ../assets/images/Greedy1.svg
---
name: actividades1
---
Lista de actividades
```

A continuación el diagrama de actividades. En principio no hay ninguna actividad seleccionada.

```{figure} ../assets/images/Greedy2.svg
---
name: actividades2
---
Diagrama de actividades
```

Paso 1
: Se selecciona la tarea que termina primero de entre todas las tareas a planificar. En este caso la tarea 1. Inmeditamente las tareas 2, 3, 5, 10 se marcan como incompatibles, ya que se superponen con la tarea 1.

```{figure} ../assets/images/Greedy3.svg
---
name: actividades3
---
Diagrama de actividades
```

Paso 2
: De entre las tareas disponibles (4, 6, 7, 8, 9 y 11) se selecciona la tarea 4, que es la que finaliza primero, por lo tanto las tareas 6 y 7 dejan de ser compatibles con la planificación.

```{figure} ../assets/images/Greedy4.svg
---
name: actividades4
---
Diagrama de actividades
```

Paso 3
: Se selecciona la tarea 8, ya que es la que finaliza primero entre las tareas disponibles (8, 9 y 11). La tarea 9 se vuelve incompatible.

```{figure} ../assets/images/Greedy5.svg
---
name: actividades5
---
Diagrama de actividades
```

Paso 4
: Por último se selecciona la única tarea disponible, la 11.

```{figure} ../assets/images/Greedy6.svg
---
name: actividades6
---
Diagrama de actividades
```

El algoritmo ávido para este problema es el siguiente:

````{prf:algorithm} Plan de actividades
**Entrada** : Lista de actividades ordenadas por tiempo de finalización

**Salida** : Lista de actividades seleccionadas

```{code-block}
---
linenos: true
---
actividades_seleccionadas := []
actividad_actual := actividades[0]
actividades_seleccionadas = append(actividades_seleccionadas, actividad_actual)
PARA CADA actividad EN actividades HACER
    SI actividad_inicio >= actividad_actual_fin ENTONCES
        actividades_seleccionadas = append(actividades_seleccionadas, actividad)
        actividad_actual := actividad
    FIN_SI
FIN_PARA
```

```{Admonition} Observación
Como la lista de entrada de las tareas está ordenada por tiempo de finalización, no hace falta programar la ecuación [](#compatibilidad2)
```

````

## Ejercicios

1. **Cambio de moneda**: Implementar en Go en forma recursiva, el algoritmo ávido para el cambio de moneda. Analizar la complejidad del algoritmo.
2. **Plan de actividades**: Implementar en Go en forma recursiva, el algoritmo ávido para el plan de actividades. Analizar la complejidad del algoritmo.
