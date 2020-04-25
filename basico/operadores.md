# Operadores Python



## Operadores de atribuição

|Operador|Sintaxe |Descrição         |Resultado   |
|:-:     |:-:     |:-                |:-:         |
|`=`     |`a = 2` |`a` recebe `2`    |`a` vale `2`|

As operações de atribuição de valor respeitam a ordem da direita para a esquerda e podem ser acumuladas.

```
 a = b = c = 125
```

`a` é igual à `b`, que é igual à `c` e que por sua vez vale `125`.

Logo, `a` vale `125`, ou ainda:

```py 
a, b, c = 125 
```
::
### Atribuição múltipla

```py 
a, b, c = 125, 126, 120
```

`a`, `b` e `c` valem `125`, `126` e `120` respectivamente.

## Operadores matemáticos

|Operador|Sintaxe |Descrição                 |Resultado|
|:-:     |:-:     |:-                        |:-:      |
|`+`     |`5 + 2` |`5` mais `2`              |   7     |
|`-`     |`5 - 2` |`5` menos `2`             |   3     |
|`*`     |`5 * 2` |`5` vezes `2`             |   10    |
|`:`     |`5 : 2` |`5` dividido por `2`      |   2.5   |
|`**`    |`5 ** 2`|`5` elevado à `2`         |   25    |
|`//`    |`5 // 2`|parte inteira de `5` dividido por `2`|2|
|`%`     |`5 % 2` |resto da divisao de `5` por `2`|1|

## Operadores Relacionais

|Operador|Sintaxe |Descrição                 |Resultado|
|:-:     |:-:     |:-                        |:-:      |
|`>`     |`5 > 2` |`5` é maior do que `2`    |True     |
|`<`     |`2 < 8` |`2` é menor do que `8`    |True     |
|`>=`    |`5 >= 2`|`5` é maior ou igual a `2`|True     |
|`>=`    |`5 >= 5`|`5` é maior ou igual a `5`|True     |
|`<=`    |`2 <= 8`|`2` é menor ou igual a `8`|True     |
|`<=`    |`2 <= 2`|`2` é menor ou igual a `2`|True     |
|`==`    |`2 == 2`|`2` é igual a `2`         |True     |

## Operadores Lógicos

|Operador|Sintaxe |Descrição                 |Resultado|
|:-:     |:-:     |:-                        |:-:      |
|`and`   |`True and True` |`True` e `True`   |True     |
|`or`    |`True or False` |`True` ou `False` |True     |

## Operadores de agregação

Considerando: `a = 6`

|Operador|Sintaxe |Descrição                 |Resultado|
|:-:     |:-:     |:-                        |:-:      |
|`+=`    |`a += 1`|`a` = `a + 1` = `7`       |a = `7`  |
|`-=`    |`a -= 1`|`a` = `a - 1` = `5`       |a = `5`  |
|`*=`    |`a *= 1`|`a` = `a * 2` = `12`      |a = `12` |
|`/=`    |`a /= 1`|`a` = `a / 2` = `3`       |a = `3`  |
|`%=`    |`a %= 1`|`a` = `a % 5` = `1`       |a = `1`  |