# Iniciando codificação

## Calculo de Fibonnaci até 10

### Algoritmo

```py
seq = []
a, b = 0, 1
while a < 10:
    seq.append(a)
    a, b = b, a+b

# seq = [0, 1, 1, 2, 3, 5, 8]
```

## Criando uma função para realizar este calculo

```py
def fibonnati():
    seq = []
    a, b = 0, 1
    while a < 10:
        seq.append(a)
        a, b = b, a+b
    return seq

# fibonnati() = [0, 1, 1, 2, 3, 5, 8]
```

## Expandindo a função para definir o maior numero
```py
def fibonnati(max):
    seq = []
    a, b = 0, 1
    while a < max:
        seq.append(a)
        a, b = b, a+b
    return seq

# fibonnati(100) = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

## Atribuindo um valor padrão de 10 para o parametro de entrada
```py
def fibonnati(max = 10):
    seq = []
    a, b = 0, 1
    while a < max:
        seq.append(a)
        a, b = b, a+b
    return seq

# fibonnati() = [0, 1, 1, 2, 3, 5, 8]
```