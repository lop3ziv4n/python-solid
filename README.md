# SOLID

####[The Coder Cave esp](https://www.youtube.com/watch?v=lUPvI-Kv9UI)
####[hdeleao.net](https://www.youtube.com/watch?v=pGYHeYig19Q&list=PLWYKfSbdsjJjk_kK-fYcjoYF_TS8_kysZ&index=1&t=1s)
####[example](https://www.enmilocalfunciona.io/principios-solid/)
####[example 2](https://softwarecrafters.io/python-3/principios-solid-python/)

## Single Responsibility Principle (SRP)
> Nunca debería haber más de un motivo por el cual cambiar una clase
> Principio de responsabilidad única, viene a decir que una clase debe tener tan solo una única responsabilidad.

## Open-Closed Principle (OCP)
> Establece que las entidades software (clases, módulos y funciones) deberían estar abiertos para su extensión, pero cerrados para su modificación.

## Liskov Substitution Principle (LSP)
> Las funciones que utilicen punteros o referencias a clases base deben ser capaces de usar objetos de clases derivadas sin saberlo.
> Es decir, una instancia de una clase B, siendo esta un subtipo de una clase A, debemos poder sustituirla por una instancia de la clase A sin mayor problema.

## Interface Segregation Principle (ISP)
> Los clientes no deberían estar obligados a depender de interfaces que no utilicen.
> El principio de segregación de la interfaz nos indica que ninguna clase debería depender de métodos que no usa. Cuando creemos interfaces que definan comportamientos, es importante estar seguros de que todas los objetos que implementen esas interfaces/clases se vayan a necesitar, de lo contrario, es mejor tener varias interfaces/clases pequeñas.

## Dependency Inversion Principle (DIP)
> Los módulos de alto nivel no deben depender de módulos de bajo nivel. Ambos deben depender de abstracciones
> Las abstracciones no deben depender de concreciones. Los detalles deben depender de abstracciones.
> Este principio viene a decir que las clases de las capas superiores no deberían depender de las clases de las capas inferiores, sino que ambas deberían depender de abstracciones. A su vez, dichas abstracciones no deberían depender de los detalles, sino que son los detalles los que deberían depender de las mismas.