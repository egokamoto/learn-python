# Aprendendo Python

## Execução básica

console python
```
py
print("Hello World")
Ctrl-Z + <Enter>
```

powershell
```
"print('Hello World')" | Out-File -Encoding "UTF8" my-script-file.py
py .\my-script-file.py <Enter>
```

bash
```
echo "print('Hello World')" | tee -a my-script-file.py > /dev/null
py my-script-file.py
```

## Sintaxe

### Inicialização de variáveis

A inicialização de variáveis é sempre necessária, nunca automatica. 

#### Atribuição de valor

A atribuição de valor se dá pelo operador `=`
```
mensagem = "Hello World"
print(mensagem)
```

### Blocos de código

Os blocos de codigo são definidos por identação

### Comentários

"""
comentário linha 1
comentário linha 2
comentário linha 3
"""

""" comentário linha única """

### Tipos de Dados

int, long, float, complex, str, unicode, list, tuple, dict, file, bool, set, frozenset
 
