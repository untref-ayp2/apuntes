---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Algoritmos Ávidos

Los algoritmos ávidos o _greedy_ en inglés, son algoritmos diseñados generalmente para resolver problemas de optimización. Un algoritmo ávido o codicioso siempre hace la elección que parece mejor en el momento. Es decir, hace una elección localmente óptima con la esperanza de que esta elección conduzca a una solución globalmente óptima.

La estrategia ávida no siempre funciona, depende de la naturaleza del problema y de los datos, por lo que hay analizar bien el problema antes de seguir esta estrategia.

La principal ventaja de este tipo de algoritmos es que es muy fácil de implementar y entender

Por ejemplo veamos el problema del cambio que se puede enunciar así:

:::{card} Problema del cambio de moneda
Un cajero automático tiene que ser capaz de dar la cantidad de pesos que se le requiere utilizando la menor cantidad de billetes y monedas
+++
**Optimización**:  entregar la menor cantidad de monedas y billetes
:::

En Argentina, a Mayo de 2024 se emplean monedas de 1, 2, 5 y 10 pesos, y billetes de 10, 20, 50, 100, 200, 500, 1.000, 2.000 y 10.000 pesos. Si el cajero tiene que entregar $ 5.528

Paso Ávido
: Entregar la mayor cantidad posible de los billetes de mayor denominación.

La solución será:
```{math}
2 \times $2000 + 1 \times $1000 + 1 \times $500 + 1 \times $20 + 1 \times $5 + 1 \times $2 +1 \times $1
```
En total se entregan 8 piezas

::::{prf:algorithm} Cambio de moneda
**Entrada**

- `billetes`: lista con las denominaciones disponibles ordenada de mayor a menor.
- `cantidad`: monto a cambiar

**Salida**

- `cambio`  : diccionario cuyas claves son las denominaciones y cuyo valor son las cantidades a entregar de cada denominación

:::{code-block}
:linenos:
PARA CADA denominacion EN billetes HACER
    // Si la cantidad restante es mayor o igual a la denominación actual
    SI cantidad >= denominacion ENTONCES
      // Calcular cuántos billetes de esta denominación se pueden usar
      cantidad_billetes := cantidad / denominacion
      // Almacenar la cantidad de billetes en el mapa de cambio
      cambio[denominacion] := cantidad_billetes
      // Actualizar la cantidad restante calculando el módulo
      cantidad := cantidad MOD denominacion
    FIN_SI
  FIN_PARA
:::
::::

A partir de este fragmento nos podemos preguntar:

1. ¿Siempre puede entregar el cambio solicitado?

2. ¿Siempre entrega la menor cantidad de billetes?

Para que siempre pueda entregar el monto solicitado, es preciso contar con el billete de 1 y que las denominaciones estén ordenadas de mayor a menor

Para asegurar que siempre da la menor cantidad de billetes, el sistema de denominaciones debe ser canónico. Es decir las denominaciones no pueden ser cualquieras, sin que deben ser un conjunto que asegure que siempre funciona el algoritmo ávido.

La comprobación de que siempre funciona se realiza con otras técnicas.

Por ejemplo si las denominaciones fueran: 1, 2, 5, 10, 20, 50, 100, 200, 500, 800 y 1.000 y tiene que dar $2.400, nuestro algoritmo ávido daría 2 x $1.000 + 2 x $200 en lugar de dar 3 billetes de $800.
