import tabuleiro

matriz_tabuleiro = tabuleiro.criar_tabuleiro()
tabuleiro.mostrar_tabuleiro(matriz_tabuleiro)

x1 = 7
y1 = 1  
x2 = 1
y2 = 1  

if(tabuleiro.posicao_valida(x1, y1, x2, y2, matriz_tabuleiro)):
   matriz_tabuleiro = tabuleiro.mover_peca(x1-1, y1-1, x2-1, y2-1, matriz_tabuleiro)
else:
   print("VOCÊ NÃO PODE FAZER ISSO!")

tabuleiro.mostrar_tabuleiro(matriz_tabuleiro)