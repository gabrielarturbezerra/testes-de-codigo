"""Estágio Ribeirão Preto - 2024

Respostas do teste online para vaga de estágio pela Gupy

Questão 2 - Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
Resposta:"""

def fibonacci(n):
    a, b = 0, 1
    fibonacci_sequence = [a, b]
    while b < n:
        a, b = b, a + b
        fibonacci_sequence.append(b)
    if n in fibonacci_sequence:
        return True, fibonacci_sequence
    else:
        return False, fibonacci_sequence

numero = int(input("Informe um número: "))
pertence, sequencia = fibonacci(numero)
if pertence:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
    print("Sequência de Fibonacci até o número informado:", sequencia)
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
    print("Sequência de Fibonacci até o número informado:", sequencia)

"""Questão 5 - Escreva um programa que inverta os caracteres de um string.
IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;"""

def inverter_string(s):
    nova_string = ''
    for i in range(len(s)-1, -1, -1):
        nova_string += s[i]
    return nova_string

string_original = input("Informe uma string: ")
string_invertida = inverter_string(string_original)
print("String invertida:", string_invertida)
