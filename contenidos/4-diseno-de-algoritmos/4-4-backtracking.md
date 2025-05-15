---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Backtracking (Vuelta Atrás)

Backtracking es una técnica algorítmica para resolver problemas donde la solución se construye probando posibilidades paso a paso y descartando caminos inviables. Siempre que el problema tenga solución con esta técnica se encontrará al costo de no ser la más eficiente.

Se utiliza comúnmente en problemas de decisión, combinatoria y optimización. La idea es construir una solución parcial y, si se encuentra un punto donde no se puede continuar, retroceder y probar otra opción.



A continuación se muestra la estructura general de este esquema:

```{code-block}
:linenos:
funcion backtracking(solución_parcial, ...)
  si es_solución(solución_parcial) entonces
    mostrar(solución_parcial)
    terminar
  sino
    para cada opción posible de extender solución_parcial hacer
      si es_factible(opción) entonces
        registrar(solución_parcial, opción)  // agregar opción a la solución parcial
        backtracking(solución_parcial, ...)  // llamada recursiva
        borrar(opción, solución_parcial)  // vuelta atrás
```