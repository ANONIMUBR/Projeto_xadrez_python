def criar_tabuleiro() -> list:
   """
   RETORNO
      :list - UMA MATRIZ COM A DISPOSIÇÃO DAS PEÇAS EM UMA MATRIZ 8X8 QUE REPRESENTA O TABULEIRO;
   
   O PRIMEIRO DÍGITO É A INICIAL DA PEÇA E O SEGUNDO INDICA SUA COR;
   q - queen;
   k - king
   """
   tabuleiro = [
      ["tp", "cp", "bp", "qp", "kp", "bp", "cp", "tp"],
      ["pp", "pp", "pp", "pp", "pp", "pp", "pp", "pp"],
      ["", "", "", "", "", "", "", ""],
      ["", "", "", "", "", "", "", ""],
      ["", "", "", "", "", "", "", ""],
      ["", "", "", "", "", "", "", ""],
      ["pb", "pb", "pb", "pb", "pb", "pb", "pb", "pb"],
      ["tb", "cb", "bb", "qb", "kb", "bb", "cb", "tb"]
   ]
   return tabuleiro


def mostrar_tabuleiro(tabuleiro: list):
   """
   PECAS:
      PRETAS: ♜ ♞ ♝ ♛ ♚ ♟ ██
      BRANCAS: ♖ ♘ ♗ ♕ ♔ ♙ ░░

   RECEBE A MATRIZ QUE CONTROLA O TABULEIRO E A CONVERTE EM UM FORMATO VISUAL MAIS AGRADÁVEL;
   """
   pecas = {
      "tp": "♜ ",
      "tb": "♖ ",
      "cp": "♞ ",
      "cb": "♘ ",
      "bp": "♝ ",
      "bb": "♗ ",
      "qp": "♛ ",
      "qb": "♕ ",
      "kp": "♚ ",
      "kb": "♔ ",
      "pp": "♟ ",
      "pb": "♙ ",
      "e_preto": "██",
      "e_branco": "░░"
   }
   print("   1 2 3 4 5 6 7 8\n --------------------")
   for i in range(len(tabuleiro)):
      linha = ""
      for j in range(len(tabuleiro[i])):
         if(tabuleiro[i][j]):
            linha += pecas[tabuleiro[i][j]]
         else:
            if(i % 2 == 0):
               linha += pecas["e_branco"] if j % 2 == 0 else pecas["e_preto"]
            else:
               linha += pecas["e_preto"] if j % 2 == 0 else pecas["e_branco"]
      print(f'{i+1}|{linha}')

def posicao_valida(x1: int, y1: int, x2: int, y2: int, tab: list) -> bool:
   return (1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8) and tab[x1-1][y1-1]


def posicao_valida(x1: int, y1: int, x2: int, y2: int, tab: list) -> bool:
   return (1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8
           and bool(tab[x1-1][y1-1])
           and (x1, y1) != (x2, y2))


def mover_peca(x1: int, y1: int, x2: int, y2: int, tab: list) -> list:
   tab[x2-1][y2-1] = tab[x1-1][y1-1]
   tab[x1-1][y1-1] = ""
   return tab