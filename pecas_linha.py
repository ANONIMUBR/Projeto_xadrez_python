import tabuleiro
import capturas

def movimento_torre(x1: int, y1: int, x2: int, y2: int, tab: list) -> bool:
   if (tabuleiro.posicao_valida(x1, y1, x2, y2, tab)
      and (x1 == x2 or y1 == y2)
      and caminho_livre(x1, y1, x2, y2, tab)):
      if tab[x2-1][y2-1]:
         if not capturas.captura_permitida(x1, y1, x2, y2, tab):
            return False
         capturas.captura_peca(x1, y1, x2, y2, tab)
      tabuleiro.mover_peca(x1, y1, x2, y2, tab)
      return True
   return False

def movimento_bispo(x1: int, y1: int, x2: int, y2: int, tab: list) -> bool:
   if (tabuleiro.posicao_valida(x1, y1, x2, y2, tab)
      and abs(x2 - x1) == abs(y2 - y1)
      and (x1 != x2 and y1 != y2)
      and caminho_livre(x1, y1, x2, y2, tab)):
      if tab[x2-1][y2-1]:
         if not capturas.captura_permitida(x1, y1, x2, y2, tab):
            return False
         capturas.captura_peca(x1, y1, x2, y2, tab)
      tabuleiro.mover_peca(x1, y1, x2, y2, tab)
      return True
   return False


def movimento_dama(x1: int, y1: int, x2: int, y2: int, tab: list) -> bool:
   if (tabuleiro.posicao_valida(x1, y1, x2, y2, tab)
      and (x1 != x2 or y1 != y2)
      and (x1 == x2 or y1 == y2 or abs(x2 - x1) == abs(y2 - y1))
      and caminho_livre(x1, y1, x2, y2, tab)):
      if tab[x2-1][y2-1]:
         if not capturas.captura_permitida(x1, y1, x2, y2, tab):
            return False
         capturas.captura_peca(x1, y1, x2, y2, tab)
      tabuleiro.mover_peca(x1, y1, x2, y2, tab)
      return True
   return False

def caminho_livre(x1: int, y1: int, x2: int, y2: int, tab: list) -> bool:
    passo_x = (x2 > x1) - (x2 < x1)
    passo_y = (y2 > y1) - (y2 < y1)

    x, y = x1 + passo_x, y1 + passo_y
    while (x, y) != (x2, y2):
        if tab[x-1][y-1]:
            return False
        x += passo_x
        y += passo_y
    return True