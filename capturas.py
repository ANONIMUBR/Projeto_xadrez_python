import tabuleiro
import pecas_linha

def movimento_rei(x1: int, y1: int, x2: int, y2: int, tab: list) -> bool:
   if (tabuleiro.posicao_valida(x1, y1, x2, y2, tab)
         and max(abs(x2 - x1), abs(y2 - y1)) == 1
         and pecas_linha.caminho_livre(x1, y1, x2, y2, tab)):
      if tab[x2-1][y2-1]:
         if not captura_permitida(x1, y1, x2, y2, tab):
            return False
         captura_peca(x1, y1, x2, y2, tab)
      tabuleiro.mover_peca(x1, y1, x2, y2, tab)
      return True
   return False


def movimento_cavalo(x1: int, y1: int, x2: int, y2: int, tab: list) -> bool:
   if (tabuleiro.posicao_valida(x1, y1, x2, y2, tab)
         and (abs(x2 - x1), abs(y2 - y1)) in [(1, 2), (2, 1)]):
      if tab[x2-1][y2-1]:
         if not captura_permitida(x1, y1, x2, y2, tab):
            return False
         captura_peca(x1, y1, x2, y2, tab)
      tabuleiro.mover_peca(x1, y1, x2, y2, tab)
      return True
   return False


def mesma_cor(x1: int, y1: int, x2: int, y2: int, tab: list) -> bool:
   origem = tab[x1-1][y1-1]
   destino = tab[x2-1][y2-1]
   return origem[1] == destino[1]


def captura_permitida(x1: int, y1: int, x2: int, y2: int, tab: list) -> bool:
   destino = tab[x2-1][y2-1]
   return bool(destino) and not mesma_cor(x1, y1, x2, y2, tab)

def captura_peca(x1: int, y1: int, x2: int, y2: int, tab: list):
   tab[x2-1][y2-1] = ""