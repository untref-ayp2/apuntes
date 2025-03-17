---
file_format: mystnb
kernelspec:
  name: gophernotes
---

# Funciones

Java no cuenta con el concepto de función como un componente independiente. En
Go las funciones pueden ser independientes del contexto y no es necesario que
sean definidas como un método estático de una clase para poder empaquetar
comportamiento. Las funciones en Go son "ciudadanos de primera clase", es decir
que una función es un valor, es decir que puedo almacenar una función en una
variable y pasarla como argumento de otra función o devolver una función como
resultado de alguna función.

Una función puede tomar cero o más argumentos, y puede devolver cero o más
valores.

```{code-cell} go
func sumar(x int, y int) int {
    return x + y
}
```

En este ejemplo la función `sumar` toma 2 parámetros de tipo `int`. Si
quisiéramos generar algo similar en Java deberíamos declarar una clase con
métodos estáticos:

```java
public class Matematica {
    public static int sumar(int a, int b) {
        return a + b;
    }
}
```

Cabe destacar, que a diferencia de Java, el valor de retorno en la declaración
de la función viene después de los paréntesis.

En Go es posible, devolver múltiples valores de una función, lo cual es muy
utilizado para el reporte de errores o la notificación del resultado de un
computo, cómo cuando se busca un valor por una clave en un `map`. Por ejemplo:

```{code-cell} go
import "errors"

func division_segura(dividendo, divisor float32) (float32, error) {
    if divisor == 0.0 {
        return 0.0, errors.New("división por cero")
    }

    return dividendo / divisor, nil
}
```

Cuando devolvemos múltiples valores los tipos devueltos se encierra entre
paréntesis, en el orden correspondiente.
