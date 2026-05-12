---
label: funciones
---

# Funciones

A diferencia de Java, donde las funciones siempre pertenecen a una clase, en Go las funciones pueden ser independientes y no es necesario definirlas como métodos estáticos. Las funciones en Go son "ciudadanos de primera clase": una función es un valor que se puede almacenar en una variable, pasar como argumento o devolver como resultado de otra función.

Una función puede tomar cero o más argumentos, y puede devolver cero o más valores.

```go
func sumar(x int, y int) int {
    return x + y
}
```

En este ejemplo la función `sumar` toma 2 parámetros de tipo `int`. Si quisiéramos generar algo similar en Java deberíamos declarar una clase con métodos estáticos:

```java
public class Matemática {
    public static int sumar(int a, int b) {
        return a + b;
    }
}
```

Cabe destacar, que a diferencia de Java, el valor de retorno en la declaración de la función viene después de los paréntesis.

En Go es posible devolver múltiples valores de una función, lo cual es muy utilizado para el reporte de errores o la notificación del resultado de un cómputo, como cuando se busca un valor por una clave en un `map`. Por ejemplo:

```go
import "errors"

func divisionSegura(dividendo, divisor float32) (float32, error) {
    if divisor == 0.0 {
        return 0.0, errors.New("división por cero")
    }

    return dividendo / divisor, nil
}
```

Cuando devolvemos múltiples valores los tipos devueltos se encierran entre paréntesis, en el orden correspondiente.
