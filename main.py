import tabuleiro
import pecas_linha
import capturas
import peao
import os

def limpar_tela():
   os.system("cls" if os.name == "nt" else "clear")

def ler_int(msg: str) -> int | None:
   try:
      return int(input(msg))
   except ValueError:
      return None

matriz_tabuleiro = tabuleiro.criar_tabuleiro()
turno = "b"
mensagem = ""

while True:
   limpar_tela()
   tabuleiro.mostrar_tabuleiro(matriz_tabuleiro)
   print(f"\nTurno: {'BRANCAS' if turno == 'b' else 'PRETAS'}")
   if mensagem:
      print(mensagem)
      mensagem = ""

   x1 = ler_int("SUA PEÇA(X): ")
   y1 = ler_int("SUA PEÇA(Y): ")
   x2 = ler_int("DESTINO(X): ")
   y2 = ler_int("DESTINO(Y): ")

   if not tabuleiro.posicao_valida(x1, y1, x2, y2, matriz_tabuleiro):
      mensagem = "Posição inválida."
      continue

   if not peao.controlar_turno(x1, y1, matriz_tabuleiro, turno):
      mensagem = "Essa peça não é sua."
      continue

   movimentos = {
      "t": pecas_linha.movimento_torre,
      "c": capturas.movimento_cavalo,
      "b": pecas_linha.movimento_bispo,
      "q": pecas_linha.movimento_dama,
      "k": capturas.movimento_rei,
      "p": peao.movimento_peao,
   }

   peca = matriz_tabuleiro[x1-1][y1-1][0]
   if movimentos[peca](x1, y1, x2, y2, matriz_tabuleiro):
      turno = peao.trocar_turno(turno)
   else:
      mensagem = "Movimento inválido!"