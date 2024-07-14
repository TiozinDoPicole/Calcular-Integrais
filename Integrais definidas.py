# Função que define a função a ser integrada
def f(x):
    # Exemplo: integrar x^2 + x
    return x**2 + x

# Função para calcular a integral definida usando o método da soma de Riemann
def integral_definida(funcao, a, b, n):
    h = (b - a) / n  # largura de cada subintervalo
    integral = 0.0

    for i in range(n):
        x_left = a + i * h  # limite esquerdo do subintervalo
        x_right = x_left + h  # limite direito do subintervalo
        x_mid = (x_left + x_right) / 2  # ponto médio do subintervalo
        integral += funcao(x_mid) * h  # área do retângulo: altura * largura

    return integral

# Solicita ao usuário a função a ser integrada
funcao_str = input("Digite a função a ser integrada (em termos de 'x'): ")

# Avalia a expressão da função e cria a função correspondente
def funcao(x):
    return eval(funcao_str)

# Solicita ao usuário os limites de integração
a = float(input("Digite o limite inferior da integral: "))
b = float(input("Digite o limite superior da integral: "))

# Solicita ao usuário o número de subintervalos
n = int(input("Digite o número de subintervalos: "))

# Calcula a integral definida
resultado = integral_definida(funcao, a, b, n)

print("O resultado da integral definida é:", resultado)
