import capturas
import tabuleiro
import pecas_linha
def movimento_peao(x1: int, y1: int, x2: int, y2: int, tab: list) -> bool:
   if not tabuleiro.posicao_valida(x1, y1, x2, y2, tab):
      return False

   cor = tab[x1-1][y1-1][1]
   direcao = 1 if cor == "p" else -1
   linha_inicial = 2 if cor == "p" else 7
   dx = x2 - x1
   dy = abs(y2 - y1)
   destino = tab[x2-1][y2-1]

   if dy == 0 and not destino:
      if dx == direcao or (dx == 2 * direcao and x1 == linha_inicial
                           and pecas_linha.caminho_livre(x1, y1, x2, y2, tab)):
         tabuleiro.mover_peca(x1, y1, x2, y2, tab)
         return True

   elif dy == 1 and dx == direcao and destino and capturas.captura_permitida(x1, y1, x2, y2, tab):
      capturas.captura_peca(x1, y1, x2, y2, tab)
      tabuleiro.mover_peca(x1, y1, x2, y2, tab)
      return True
   return False


def controlar_turno(x1: int, y1: int, tab: list, turno: str) -> bool:
   if not (1 <= x1 <= 8 and 1 <= y1 <= 8):
      return False
   peca = tab[x1-1][y1-1]
   return bool(peca) and peca[1] == turno


def trocar_turno(turno: str) -> str:
   return "b" if turno == "p" else "p"