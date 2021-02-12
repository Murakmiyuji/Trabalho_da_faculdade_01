import math
import numpy as np
import turtle

"""
INICIADO: 10/02/2021.
FINALIZADO: 12/02/2021.
DESENVOLVIDO POR: YUJI FARUK MURAKAMI FELES.
Neste modulo encontra-se as funções pertinentes para elaboração do programa principal.
Funções como: criar_arquivo_txt; desenhar_triangulo; separador_de_str_2elementos; separador_de_str_3elementos; 
    ler_arquivo_txt;
Enjoy! :)
"""

def criar_arquivo_txt(arquivo):

    with open(arquivo, 'w') as f:

        #Primeira coordenada do Triângulo Retângulo
        while True:

            try:
                coordx = float(input("Valor da coordenada x: "))

            except ValueError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            except TypeError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')
            else:
                print('\033[34mOk! Foi adicionado o valor.\033[m')
                break

        #Segunda coordenada do Triangulo Retângulo
        while True:

            try:
                coordy = float(input("Valor da coordenada y: "))

            except ValueError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            except TypeError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            else:
                print('\033[34mOk! Foi adicionado o valor.\033[m')
                break

        #Primeiro cateto do triangulo retângulo
        while True:

            try:
                cateto1 = float(input("Valor do primeiro cateto: "))

            except ValueError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            except TypeError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            else:
                print('\033[34mOk! Foi adicionado o valor.\033[m')
                break

        #Segundo cateto do Triangulo Retângulo
        while True:

            try:
                cateto2 = float(input("Valor do segundo cateto: "))

            except ValueError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            except TypeError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            else:
                print('\033[34mOk! Foi adicionado o valor.\033[m')
                break

        #Ponto A, coordenada x
        while True:

            try:
                ponto1x = float(input("Valor da coordenada x do ponto A: "))

            except ValueError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            except TypeError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            else:
                print('\033[34mOk! Foi adicionado o valor.\033[m')
                break

        #Ponto 1, coordenada y
        while True:

            try:
                ponto1y = float(input("valor da coordenada y do ponto A: "))

            except ValueError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            except TypeError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            else:
                print('\033[34mOk! Foi adicionado o valor.\033[m')
                break

        #Cor do ponto 1
        while True:

            try:
                cor1 = str(input("Cor em inglês do ponto A: "))

            except ValueError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo string\033[m')

            except TypeError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo string\033[m')

            else:
                print('\033[34mOk! Foi adicionado o valor.\033[m')
                break

        #Ponto B, coordenada x
        while True:

            try:
                ponto2x = float(input("Valor da coordenada x do ponto B: "))

            except ValueError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            except TypeError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            else:
                print('\033[34mOk! Foi adicionado o valor.\033[m')
                break

        #Ponto B, coordenada y
        while True:

            try:
               ponto2y = float(input("valor da coordenada y do ponto B: "))

            except ValueError:
               print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            except TypeError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            else:
                print('\033[34mOk! Foi adicionado o valor.\033[m')
                break

        #Cor do ponto B
        while True:

            try:
                cor2 = str(input("Cor em inglês do ponto B: "))

            except ValueError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo string\033[m')

            except TypeError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo string\033[m')

            else:
                print('\033[34mOk! Foi adicionado o valor.\033[m')
                break

        #Ponto C, coordenada x
        while True:

            try:
                ponto3x = float(input("Valor da coordenada x do ponto C: "))

            except ValueError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            except TypeError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            else:
                print('\033[34mOk! Foi adicionado o valor.\033[m')
                break

        #Ponto C, coordenada y
        while True:

            try:
                ponto3y = float(input("valor da coordenada y do ponto C: "))

            except ValueError:
                 print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            except TypeError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            else:
                print('\033[34mOk! Foi adicionado o valor.\033[m')
                break

        #Cor do ponto C
        while True:

            try:
                cor3 = str(input("Cor em inglês do ponto C: "))

            except ValueError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo string\033[m')

            except TypeError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo string\033[m')

            else:
                print('\033[34mOk! Foi adicionado o valor.\033[m')
                break

        #Ponto D, coordenada x
        while True:

            try:
                ponto4x = float(input("Valor da coordenada x do ponto D: "))

            except ValueError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            except TypeError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')
            else:
                print('\033[34mOk! Foi adicionado o valor.\033[m')
                break

        #Ponto D, coordenada y
        while True:

            try:
                ponto4y = float(input("valor da coordenada y do ponto D: "))

            except ValueError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            except TypeError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            else:
                print('\033[34mOk! Foi adicionado o valor.\033[m')
                break

        #Cor do ponto D
        while True:

            try:
                cor4 = str(input("Cor em inglês do ponto D: "))

            except ValueError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            except TypeError:
                print('\033[31mErro no tipo de informação inserida. Lembre-se somente do tipo float\033[m')

            else:
                print('\033[34mOk! Foi adicionado o valor.\033[m')
                break

        #Junção das informações em respectivas linhas
        primeira_linha = (str(coordx) + ' ' + str(coordy))
        quarta_linha   = (str(ponto1x) + ' ' + str(ponto1y) + ' ' + str(cor1) + ' ')
        quinta_linha   = (str(ponto2x) + ' ' + str(ponto2y) + ' ' + str(cor2) + ' ')
        sexta_linha    = (str(ponto3x) + ' ' + str(ponto3y) + ' ' + str(cor3) + ' ')
        setima_linha   = (str(ponto4x) + ' ' + str(ponto4y) + ' ' + str(cor4) + ' ')

        #Comando para escrever dentro do arquivo
        f.write(primeira_linha + '\n')
        f.write(str(cateto1) + '\n')
        f.write(str(cateto2) + '\n')
        f.write(quarta_linha + '\n')
        f.write(quinta_linha + '\n')
        f.write(sexta_linha + '\n')
        f.write(setima_linha + '\n')

def desenhar_triangulo(matriz_triangular,matriz_ponto1,matriz_ponto2,matriz_ponto3,matriz_ponto4):

    #Define os valores de x, y, cateto1, cateto2
    x = matriz_triangular[0]
    y = matriz_triangular[1]

    cateto1 = matriz_triangular[2]
    cateto2 = matriz_triangular[3]

    # Aumenta o tamanho da tela gráfica para 1000x1000
    turtle.screensize(1000, 1000)

    # Cria o turtle
    turtle.Turtle()

    # Determina o tamanho da caneta
    turtle.pensize(3)

    # Determina a direção da tartaruga
    turtle.setheading(0)

    # Levanta a caneta para não rabiscar
    turtle.penup()

    # Determina a posição onde a tartaruga deve ficar
    turtle.setpos(x,y)

    # Armazena a posição da tartaruga
    posinicial = turtle.pos()

    # Desce a caneta para rabiscar
    turtle.pendown()

    # Ordena andar <cateto1> de distancia
    turtle.fd(cateto1)

    # Ordena virar 90 graus a esquerda
    turtle.left(90)

    # Ordena andar <cateto2> de distancia
    turtle.fd(cateto2)

    # Teorema de Pitágoras a²=b²+c²
    hipotenusa = float(math.sqrt(cateto1**2 + cateto2**2))

    # Tangente = Oposto / Adjacente ; ArcoTangente para saber o grau
    angulo_alfa = float(math.atan(cateto1/cateto2))

    # Conversor de Radianos para graus
    angulo_alfa = float(math.degrees(angulo_alfa))

    #Diferença para saber o angulo externo
    angulo = 180 - angulo_alfa

    #Rotaciona a tartaruga para fechar o triangulo retangulo
    turtle.left(angulo)

    #1: Se o triângulo estiver no primeiro quadrante do plano cartesiano, então:
    if x < cateto1 and y < cateto2:
        turtle.left(angulo)

    #2: Se o triângulo estiver no quarto quadrante do plano cartesiano, então:
    elif x < cateto1 and y > cateto2:
        turtle.left(angulo_alfa)

    #3: Se o triângulo estiver no quarto segundo quadrante do plano cartesiano, então:
    elif x > cateto1 and y < cateto2:
        turtle.right(angulo)

    #4: Se o triângulo estiver no quarto terceiro quadrante do plano cartesiano, então:
    elif x > cateto1 and y > cateto2:
        turtle.left(angulo_alfa)

    # Ordena andar <hipotenusa> de distancia
    turtle.fd(hipotenusa)

    #Armazena a posição da tartaruga na variavel
    posfinal = turtle.pos()

    #Condicional para saber se o triangulo foi formado ou não.
    if posfinal == posinicial:
        print("Triangulo Retângulo formado! Cateto oposto {}, cateto adjacente {}, hipotenusa {} e angulo {}".
              format(cateto1,cateto2,hipotenusa,angulo_alfa))
    elif posfinal != posinicial:
        print('Triangulo Retângulo não formado!')
        print("Posição final {}, Posição inicial{}".format(posfinal, posinicial))

    #Movimenta e cria o primeiro ponto
    x1 = float(matriz_ponto1[0])
    y1 = float(matriz_ponto1[1])

    cor1 = str(matriz_ponto1[2])

    turtle.penup()
    turtle.setposition(x1,y1)
    turtle.pendown()
    turtle.dot(30, cor1)

    #Movimenta e cria o segundo ponto
    x2 = float(matriz_ponto2[0])
    y2 = float(matriz_ponto2[1])

    cor2 = str(matriz_ponto2[2])

    turtle.penup()
    turtle.setposition(x2, y2)
    turtle.pendown()
    turtle.dot(30, cor2)

    #Movimenta e cria o terceiro ponto
    x3 = float(matriz_ponto3[0])
    y3 = float(matriz_ponto3[1])

    cor3 = str(matriz_ponto3[2])

    turtle.penup()
    turtle.setposition(x3, y3)
    turtle.pendown()
    turtle.dot(30, cor3)

    #Movimenta e cria o quarto ponto
    x4 = float(matriz_ponto4[0])
    y4 = float(matriz_ponto4[1])

    cor4 = str(matriz_ponto4[2])

    turtle.penup()
    turtle.setposition(x4, y4)
    turtle.pendown()
    turtle.dot(30, cor4)

    #Calulando a média das matrizes
    matriz_ponto5x = np.array([x1,x2,x3,x4])
    matriz_ponto5y = np.array([y1,y2,y3,y4])

    x5 = float(np.median(matriz_ponto5x))
    y5 = float(np.median(matriz_ponto5y))

    print("Ponto E (5) [{}]".format(np.array([x5,y5])))

    #Movimenta e cria o quinto ponto
    turtle.penup()
    turtle.setposition(x5, y5)
    turtle.pendown()
    turtle.dot(30)

    #Comando que exige que o usuário clique no visor para sair da tela
    turtle.exitonclick()


def separador_de_str_2elementos(l):

    # Separa o conteúdo da primeira linha no espaço
    separador = l.split(' ')

    primeira_parte = float(separador[0])
    segunda_parte = float(separador[1])

    ma = np.array([primeira_parte, segunda_parte])

    return ma


def separador_de_str_3elementos(l):

    # Separa o conteúdo da primeira linha no espaço
    separador = l.split(' ')

    primeira_parte = float(separador[0])
    segunda_parte = float(separador[1])
    terceira_parte = str(separador[2])

    ma = np.array([primeira_parte, segunda_parte,terceira_parte])

    return ma


def ler_arquivo_txt(arquivo):

    #Declara estas variaveis como globais.
    global m_t, m_p1, m_p2, m_p3, m_p4

    with open(arquivo, 'r') as f:

        # primeira linha do arquivo
        linha = str(f.readline())

        matriz = separador_de_str_2elementos(linha)

        x = float(matriz[0])
        y = float(matriz[1])
        print("Coordenada x = {}, y = {}".format(x,y))

        # segunda linha do arquivo
        cateto1 = float(f.readline())

        # terceira linha do arquivo
        cateto2 = float(f.readline())

        # quarta linha do arquivo
        linha   = str(f.readline())

        matriz  = separador_de_str_3elementos(linha)

        ponto1x = float(matriz[0])
        ponto1y = float(matriz[1])

        cor1    = str(matriz[2])

        # quinta linha do arquivo
        linha   = str(f.readline())

        matriz  = separador_de_str_3elementos(linha)

        ponto2x = float(matriz[0])
        ponto2y = float(matriz[1])

        cor2    = str(matriz[2])

        # sexta linha do arquivo
        linha   = str(f.readline())

        matriz  = separador_de_str_3elementos(linha)

        ponto3x = float(matriz[0])
        ponto3y = float(matriz[1])

        cor3    = str(matriz[2])

        # sétima linha do arquivo
        linha   = str(f.readline())

        matriz  = separador_de_str_3elementos(linha)

        ponto4x = float(matriz[0])
        ponto4y = float(matriz[1])

        cor4    = str(matriz[2])

        #Criando array's para as coordenadas
        m_t      = np.array([x, y, cateto1, cateto2])
        m_p1     = np.array([ponto1x, ponto1y, cor1])
        m_p2     = np.array([ponto2x, ponto2y, cor2])
        m_p3     = np.array([ponto3x, ponto3y, cor3])
        m_p4     = np.array([ponto4x, ponto4y, cor4])

        #Chama função para calular o ponto médio entre os pontos no plano cartesiano
        desenhar_triangulo(m_t, m_p1, m_p2, m_p3, m_p4)



