## Execução básica

>console python

```
# py
print("Hello World")
>>> Hello World
Ctrl-Z + <Enter>
```

>powershell

```powershell
"print('Hello World')" | Out-File -Encoding "UTF8" my-script-file.py
py .\my-script-file.py <Enter>
```

>bash

```
# echo "print('Hello World')" | tee -a my-script-file.py > /dev/null
# py my-script-file.py
Hello World
```

## Sintaxe

### Inicialização de variáveis

A inicialização de variáveis é sempre necessária, nunca automatica. 

### Blocos de código

Os blocos de codigo são definidos por identação

```py
print('nivel 1')#primeiro nível hierárquico

if(True):
    print("nível 2")#segundo nível hierárquico
```

### Comentários
```py
"""
comentário linha 1
comentário linha 2
comentário linha 3
"""
```

```py
""" comentário linha única """
```

### Atribuindo à partir de uma entrada de dados

```py
num = input("Digite um número:")
print(num)
```

```console
>>> num = input("Digite um número:")
Digite um número:23
>>> print(num)
23
>>>
```

### Executando em linha
```py
>>> num = input("Digite um número:"); print(num)
Digite um número:12
12
```