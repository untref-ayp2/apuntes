---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
---

# Tipos Abstractos de Datos

Podemos imaginar un Tipo Abstracto de Datos (TAD) o _Abstract Data Type_ (ADT) en inglés, como una caja negra, la que puede contener valores y manipularlos, es decir realizar acciones con esos valores, por ejemplo ordenarlos, buscar un elemento dado, etc.

```{Admonition} Definición
Un TAD es un modelo matemático caracterizado por:

Un conjunto de valores
: Son los datos que se pueden manipular.

Un conjunto de operaciones
: Son las acciones que se pueden hacer sobre los datos.
```

En un TAD podemos distinguir dos capas, la estructura interna donde realmente se almacenan los datos y la interfaz que expone hacia afuera, hacia el usuario del TAD, las operaciones que se pueden realizar con esos datos.

Por ejemplo son TAD las listas, conjuntos y grafos. Se puede interactuar con estos TAD a través de un conjunto de operaciones definidas para cada uno. En un conjunto podemos chequear si un elemento pertenece al mismo, o agregar o sacar elementos. A una lista le podemos solicitar que nos pase el siguiente elemento, pero no deberíamos tener acceso a la estructura interna del TAD, es decir a la estructura de datos que sirve como contenedor para almacenarlos, y mucho menos a manipular esa estructura contenedor usando otras operaciones distintas de las que están definidas en el TAD.

Las principales características de un TAD son:

Abstracción
: En un TAD, la abstracción implica definir un conjunto de operaciones que pueden realizarse sobre un tipo de dato, sin revelar cómo se implementan estas operaciones internamente.

Ocultamiento de información
: Es el mecanismo que permite ocultar los detalles de la implementación, encapsulando los datos y las operaciones en una única estructura y exponiendo solo una interfaz bien definida.

Es decir la **abstracción** se logra mediante el **ocultamiento de información**.

Interfaz
: Es la parte visible del TAD, que define como se puede interactuar con él.

Comportamiento
: Es el conjunto de operaciones que se puede realizar en un TAD.

Es decir el **comportamiento** de un TAD se define a través de su **interfaz**

Invariante de representación
: Es una condición lógica que siempre debe cumplirse para cualquier estado válido del TAD. Es como una regla interna que garantiza la integridad y coherencia de la estructura de datos.

Por ejemplo en una lista de elementos todos los elementos tienen un sucesor y un predecesor salvo el primero y el último de la lista. El primero sólo tiene sucesor y el último sólo tiene predecesor. **Si no se cumple el invariante, entonces el TAD está "roto"**. Volviendo al ejemplo de la lista, si por algun motivo algún elemento intermedio pierde la referencia a su sucesor la lista queda inutilizable.

Go cuenta con `struct`{l=go} e `interface`{l=go} para definir nuevos tipos abstractos de datos. Las estructuras nos permiten definir un conjunto de valores y un conjunto de operaciones asociadas a esas estructuras. Algunas de las operaciones pueden ser públicas, es decir, formar parte de la interfaz del TAD o ser privadas, para uso interno. Las interfaces permiten que varios tipos de datos que presentan el mismo comportamiento puedan manipularse como un único tipo.
