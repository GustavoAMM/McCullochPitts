# McCulloch-Pitts

Este código contiene una implementación de la neurona de McCulloch-Pitts. Esta neurona es un modelo simple de una neurona artificial que se utiliza en el campo del aprendizaje automático. Esta implementación incluye lógica para entrenar y evaluar la neurona para las compuertas lógicas AND, OR y NOT.

## Requerimientos

Este código está escrito en Python 3. Para ejecutarlo, necesitarás tener Python 3 instalado en tu sistema. 

## Uso

Para utilizar esta implementación de la neurona de McCulloch-Pitts, puedes crear una instancia de la clase `McCullochPitts`. El constructor toma tres argumentos: `n_bits`, `compuerta` y `epoch`:

- `n_bits` es el número de bits que se utilizarán en la entrada 
- `compuerta` es el tipo de compuerta lógica que se utilizará para entrenar la neurona
- `epoch` es el número de épocas que se utilizarán durante el entrenamiento.

Una vez que haya creado una instancia de la clase `McCullochPitts`, puede entrenar la neurona llamando al método `entrenar`. Después de entrenar la neurona, puede evaluarla en nuevas entradas llamando al método `evaluar`.

Por ejemplo, aquí hay un ejemplo de cómo se puede utilizar esta implementación para entrenar y evaluar la neurona para la compuerta lógica OR:

```
mp = McCullochPitts(n_bits=2, compuerta="OR", epoch=100)
mp.entrenar()
mp.evaluar([0, 1])
```


Este código crearía una instancia de la clase `McCullochPitts` con dos bits de entrada y entrenaría la neurona durante 100 épocas para la compuerta lógica OR. Luego, evaluaría la neurona en la entrada `[0, 1]` y devolvería la salida de la neurona.


