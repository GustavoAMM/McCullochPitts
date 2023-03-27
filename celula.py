import random


class McCullochPitts:
    
    def __init__(self, n_bits, compuerta, epoch):
        self.n_bits = n_bits
        self.compuerta = compuerta
        self.epoch = epoch
        self.umbral = random.randint(-1, 1) #inicialización aleatoria del umbral
        self.pesos = [random.randint(1, 10) for _ in range(n_bits)] #inicialización aleatoria de los pesos

    def activacion(self, entradas):
        suma = sum([peso * entrada for peso,
                   entrada in zip(self.pesos, entradas)]) #cálculo de la suma ponderada
        return suma >= self.umbral if self.umbral <= 0 else suma == self.umbral #cálculo de la función de activación

    def entrenar(self):
        if self.compuerta == "NOT" and self.n_bits != 1: #comprobación de que la compuerta NOT solo funciona con 1 bit
            print("Compuerta NOT solo funciona con 1 bit")
            return SystemExit
        for ep in range(self.epoch): #entrenamiento
            for entrada, salida_esperada in self.tabla_verdad():
                salida_obtenida = self.activacion(entrada) #cálculo de la salida obtenida
                if salida_esperada != salida_obtenida: # si la salida obtenida es diferente a la salida esperada, se actualizan los pesos y el umbral
                    signo = 1 if salida_esperada > salida_obtenida else -1
                    self.umbral += signo
                    self.pesos = [peso + signo * entrada[i]
                                  for i, peso in enumerate(self.pesos)]
        print(f"APRENDIZAJE EXITOSO EN LA ÉPOCA:{ep}")
        print(f"valor del umbral = {self.umbral}") #se muestran los valores de los pesos y el umbral
        print(f"valor de los pesos = {self.pesos}")

    def evaluar(self, entrada):
        #comprobación de que la cantidad de bits dada es igual a la cantidad de bits entrenados
        if len(entrada) != self.n_bits:
            print("La cantidad de bits dada no es igual a el numero de bits entrenados")
            return SystemExit
        # Obtiene la salida esperada a partir de la activación de la neurona con las entradas dadas
        salida = self.activacion(entrada)
        # Obtiene la salida esperada a partir de la tabla de verdad
        salida_esperada = bool(self.tabla_verdad()[int(
            "".join(str(i) for i in entrada), 2)][1])
        # Imprime la salida esperada y la salida obtenida
        print(f'Salida esperada: {salida_esperada}')
        print(f'Salida obtenida: {salida}')
        # Retorna True si la salida esperada es igual a la salida obtenida
        return salida == salida_esperada

    def tabla_verdad(self):
        n = self.n_bits
        if self.compuerta == "AND":
            # Genera la tabla de verdad de la compuerta AND
            return [([int("{0:b}".format(i).zfill(n)[j]) for j in range(n)], int(all([int("{0:b}".format(i).zfill(n)[j]) for j in range(n)]))) for i in range(2**n)]
        elif self.compuerta == "OR":
            # Genera la tabla de verdad de la compuerta OR
            return [([int("{0:b}".format(i).zfill(n)[j]) for j in range(n)], int(any([int("{0:b}".format(i).zfill(n)[j]) for j in range(n)]))) for i in range(2**n)]
        elif self.compuerta == "NOT":
            # Genera la tabla de verdad de la compuerta NOT
            return [([0], 1), ([1], 0)]
        else:
            # Si la compuerta no es AND, OR o NOT, se muestra un mensaje de error
            print("Compuerta desconocida o en esta en minusculas")
            raise SystemExit

    def tt(self):
        # Imprime la tabla de verdad de la compuerta dada y la cantidad de bits
        for entrada, salida_esperada in self.tabla_verdad():
            salida_obtenida = self.activacion(entrada)
            salida_esperada = bool(salida_esperada)
            print(f"{entrada}:{salida_obtenida == salida_esperada}")
