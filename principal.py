import funcoes as fuc
#INICIADO: 10/02/2021
#FINALIZADO: 10/02/2021
#DESENVOLVIDO POR: YUJI FARUK MURAKAMI FELES


#Inseri o nome do arquivo.txt
arquivo = input("Nome do arquivo a ser criado: ")

#Chama a função criar arquivo
fuc.criar_arquivo_txt(arquivo)

#Chama a função ler arquivo, que irá consequentemente chamar as funções designadas para o turtle.
fuc.ler_arquivo_txt(arquivo)


