import math
import numpy as np
import turtle


def criar_arquivo_txt(arquivo):

    with open(arquivo, 'w') as f:

        #Triângulo Retângulo
        coordx = str(input("Valor da coordenada x: "))
        coordy = str(input("Valor da coordenada y: "))

        cateto1 = str(input("Valor do primeiro cateto: "))
        cateto2 = str(input("Valor do segundo cateto: "))

        #Ponto A
        ponto1x = str(input("Valor da coordenada x do ponto A: "))
        ponto1y = str(input("valor da coordenada y do ponto A: "))

        cor1 = str(input("Cor em inglês do ponto A: "))

        #Ponto B
        ponto2x = str(input("Valor da coordenada x do ponto B: "))
        ponto2y = str(input("valor da coordenada y do ponto B: "))

        cor2 = str(input("Cor em inglês do ponto B: "))

        #Ponto C
        ponto3x = str(input("Valor da coordenada x do ponto C: "))
        ponto3y = str(input("valor da coordenada y do ponto C: "))

        cor3 = str(input("Cor em inglês do ponto C: "))

        #Ponto D
        ponto4x = str(input("Valor da coordenada x do ponto D: "))
        ponto4y = str(input("valor da coordenada y do ponto D: "))

        cor4 = str(input("Cor em inglês do ponto D: "))

        primeira_linha = coordx + ' ' + coordy
        quarta_linha = ponto1x + ' ' + ponto1y + ' ' + cor1 + ' '
        quinta_linha = ponto2x + ' ' + ponto2y + ' ' + cor2 + ' '
        sexta_linha = ponto3x + ' ' + ponto3y + ' ' + cor3 + ' '
        setima_linha = ponto4x + ' ' + ponto4y + ' ' + cor4 + ' '

        f.write(primeira_linha + '\n')
        f.write(cateto1 + '\n')
        f.write(cateto2 + '\n')
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

    # Primeira Condicional para determinar para que lado é a hipotenusa
    if x < cateto1 and y < cateto2:
        turtle.left(angulo)

    # Segunda Condicional para determinar para que lado é a hipotenusa
    elif x < cateto1 and y > cateto2:
        turtle.left(angulo_alfa)

    # Terceira Condicional para determinar para que lado é a hipotenusa
    elif x > cateto1 and y < cateto2:
        turtle.right(angulo)

    # Quarta Condicional para determinar para que lado é a hipotenusa
    elif x > cateto1 and y > cateto2:
        turtle.left(angulo_alfa)

    # Ordena andar <hipotenusa> de distancia
    turtle.fd(hipotenusa)

    #Armazena a posição da tartaruga na variavel
    posfinal = turtle.pos()

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


    turtle.exitonclick()


def separador_de_str_2elementos(linha):

    # Separa o conteúdo da primeira linha no espaço
    separador = linha.split(' ')

    primeira_parte = float(separador[0])
    segunda_parte = float(separador[1])

    ma = np.array([primeira_parte,segunda_parte])

    return ma


def separador_de_str_3elementos(linha):

    # Separa o conteúdo da primeira linha no espaço
    separador = linha.split(' ')

    primeira_parte = float(separador[0])
    segunda_parte = float(separador[1])
    terceira_parte = str(separador[2])

    ma = np.array([primeira_parte, segunda_parte,terceira_parte])

    return ma


def ler_arquivo_txt(arquivo):

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

        #Função para desenhar o triangulo com o .Turtle()
        #desenhar_triangulo(x,y,cateto1,cateto2)

        # quarta linha do arquivo
        linha = str(f.readline())

        matriz = separador_de_str_3elementos(linha)

        ponto1x = float(matriz[0])
        ponto1y = float(matriz[1])

        cor1 = str(matriz[2])

        # quinta linha do arquivo
        linha = str(f.readline())

        matriz = separador_de_str_3elementos(linha)

        ponto2x = float(matriz[0])
        ponto2y = float(matriz[1])

        cor2 = str(matriz[2])

        # sexta linha do arquivo
        linha = str(f.readline())

        matriz = separador_de_str_3elementos(linha)

        ponto3x = float(matriz[0])
        ponto3y = float(matriz[1])

        cor3 = str(matriz[2])

        # sétima linha do arquivo
        linha = str(f.readline())

        matriz = separador_de_str_3elementos(linha)

        ponto4x = float(matriz[0])
        ponto4y = float(matriz[1])

        cor4 = str(matriz[2])

        #Criando array's para as coordenadas
        matriz_triangular = np.array([x,y,cateto1,cateto2])
        matriz_ponto1 = np.array([ponto1x,ponto1y,cor1])
        matriz_ponto2 = np.array([ponto2x,ponto2y,cor2])
        matriz_ponto3 = np.array([ponto3x,ponto3y,cor3])
        matriz_ponto4 = np.array([ponto4x,ponto4y,cor4])

        #Chama função para calular o ponto médio entre os pontos no plano cartesiano
        desenhar_triangulo(matriz_triangular,matriz_ponto1,matriz_ponto2,matriz_ponto3,matriz_ponto4)



