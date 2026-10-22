# PROJETO XADREZ EM PYTHON

## Projeto_xadrez_python

Para a execução do projeto basta ter um ambiente Python configurado, sendo sua última versão estável a mais indicada para este ambiente.
Com tudo configurado, execute `main.py` para jogar:

```bash
python main.py
```

> **Requisito:** o projeto usa `match/case` e a sintaxe `int | None`, portanto exige **Python 3.10 ou superior**.

## ESTRUTURA PADRÃO

```
xadrez/
│
├── main.py
├── tabuleiro.py
├── pecas_linha.py
├── capturas.py
├── peao.py
├── testes.py
├── README.md
└── relatorio.pdf
```

| Arquivo | Responsabilidade |
|---------|------------------|
| `main.py` | Ponto de entrada e laço principal do jogo |
| `tabuleiro.py` | Criação, exibição e modificação do tabuleiro |
| `pecas_linha.py` | Torre, bispo, dama e verificação de caminho livre |
| `capturas.py` | Cavalo, rei e regras de captura |
| `peao.py` | Peão e controle de turnos |
| `testes.py` | Testes automatizados das regras |
| `relatorio.pdf` | Relatório do projeto |

## COMO JOGAR

A cada rodada o programa pede quatro números, de **1 a 8**:

1. `SUA PEÇA(X)`: linha da peça que você quer mover;
2. `SUA PEÇA(Y)`: coluna da peça que você quer mover;
3. `DESTINO(X)`: linha de destino;
4. `DESTINO(Y)`: coluna de destino.

- As **brancas** começam a partida.
- Se o movimento for ilegal, uma mensagem é exibida e o mesmo jogador joga novamente.
- O `X` é a **linha** (número à esquerda do tabuleiro) e o `Y` é a **coluna** (número no topo).

## tabuleiro.py

Responsável por **criar, exibir e modificar** o tabuleiro. É o módulo base: todos os outros dependem dele.

### Representação do tabuleiro

O tabuleiro é uma matriz 8x8 (lista de listas). Cada casa é uma string:

| Valor | Significado |
|-------|-------------|
| `""` | Casa vazia |
| `"tp"` | 1º caractere = tipo da peça, 2º caractere = cor |

**Tipos de peça (1º caractere):**

| Letra | Peça |
|-------|------|
| `t` | Torre |
| `c` | Cavalo |
| `b` | Bispo |
| `q` | Dama (*queen*) |
| `k` | Rei (*king*) |
| `p` | Peão |

**Cores (2º caractere):** `p` = pretas (topo, linhas 1 e 2) e `b` = brancas (base, linhas 7 e 8).

> **Atenção:** a letra `p` aparece nos dois campos (peão no tipo, preta na cor). Por exemplo, `"pp"` é um peão preto e `"pb"` é um peão branco.

### Sistema de coordenadas

- O usuário informa coordenadas de **1 a 8**.
- `x` é a **linha** e `y` é a **coluna**.
- Internamente, o acesso à matriz usa `tab[x-1][y-1]`.

### Funções

#### `criar_tabuleiro() -> list`

Retorna uma matriz 8x8 com as peças na posição inicial.

#### `mostrar_tabuleiro(tabuleiro: list) -> None`

Imprime o tabuleiro no terminal usando símbolos Unicode.

| | Pretas | Brancas |
|---|:---:|:---:|
| Torre | ♜ | ♖ |
| Cavalo | ♞ | ♘ |
| Bispo | ♝ | ♗ |
| Dama | ♛ | ♕ |
| Rei | ♚ | ♔ |
| Peão | ♟ | ♙ |

As casas vazias alternam entre `██` (escura) e `░░` (clara), formando o padrão de xadrez.

#### `posicao_valida(x1, y1, x2, y2, tab) -> bool`

Retorna `True` somente se:

1. Todas as coordenadas estão entre 1 e 8;
2. Existe uma peça na casa de origem;
3. Origem e destino são casas diferentes.

#### `mover_peca(x1, y1, x2, y2, tab) -> list`

Copia a peça da origem para o destino e esvazia a origem. Retorna a matriz atualizada.
**Não valida regras de movimento**: isso é responsabilidade dos demais módulos.


## pecas_linha.py

Contém as peças que se movem **em linha** (torre, bispo e dama) e a função auxiliar que verifica obstáculos.

#### `movimento_torre(x1, y1, x2, y2, tab) -> bool`

Move a torre na horizontal ou vertical (`x1 == x2` ou `y1 == y2`), desde que o caminho esteja livre.

#### `movimento_bispo(x1, y1, x2, y2, tab) -> bool`

Move o bispo na diagonal (`|dx| == |dy|`), desde que o caminho esteja livre.

#### `movimento_dama(x1, y1, x2, y2, tab) -> bool`

Combina os movimentos da torre e do bispo.

#### `caminho_livre(x1, y1, x2, y2, tab) -> bool`

Percorre as casas **entre** origem e destino (sem incluí-las) e retorna `False` se encontrar alguma peça.
Usada também pelo rei e pelo avanço duplo do peão.

### Fluxo comum às três peças

1. Valida a posição e o formato do movimento;
2. Verifica se o caminho está livre;
3. Se o destino estiver ocupado, confere se a captura é permitida (peça de cor diferente) e remove a peça capturada;
4. Move a peça e retorna `True`.

Em qualquer falha, retorna `False` sem alterar o tabuleiro.

## capturas.py

Reúne os movimentos do **cavalo** e do **rei**, além das funções que controlam a **captura de peças** (usadas por todos os módulos).

#### `movimento_cavalo(x1, y1, x2, y2, tab) -> bool`

Move o cavalo em "L" (deslocamentos `(1, 2)` ou `(2, 1)`). O cavalo **salta** sobre outras peças, por isso não verifica o caminho.

#### `movimento_rei(x1, y1, x2, y2, tab) -> bool`

Move o rei uma casa em qualquer direção (`max(|dx|, |dy|) == 1`).

#### `mesma_cor(x1, y1, x2, y2, tab) -> bool`

Compara a cor da peça de origem com a do destino.

#### `captura_permitida(x1, y1, x2, y2, tab) -> bool`

Retorna `True` se o destino está ocupado **e** por uma peça de cor diferente.

#### `captura_peca(x1, y1, x2, y2, tab) -> None`

Remove a peça que está na casa de destino (`tab[x2-1][y2-1] = ""`).

---

## peao.py

Contém as regras do **peão** e o **controle de turnos**.

#### `movimento_peao(x1, y1, x2, y2, tab) -> bool`

O peão tem regras próprias, pois anda de um jeito e captura de outro:

| Situação | Regra |
|----------|-------|
| Avanço simples | 1 casa à frente, na mesma coluna, com o destino vazio |
| Avanço duplo | 2 casas à frente, só a partir da linha inicial, com caminho livre |
| Captura | 1 casa na diagonal à frente, com peça adversária no destino |

A direção depende da cor: peças pretas **descem** (+1) e peças brancas **sobem** (-1).
A linha inicial é 2 para as pretas e 7 para as brancas.

#### `controlar_turno(x1, y1, tab, turno) -> bool`

Retorna `True` se a peça selecionada pertence ao jogador da vez.

#### `trocar_turno(turno) -> str`

Alterna entre `"b"` (brancas) e `"p"` (pretas).

## main.py

Ponto de entrada do jogo. Contém o laço principal, que a cada rodada:

1. Limpa a tela e exibe o tabuleiro e o turno atual;
2. Lê as coordenadas de origem e destino (`ler_int` trata entradas inválidas);
3. Valida a posição e verifica se a peça pertence ao jogador da vez;
4. Chama a função de movimento correspondente ao tipo da peça, usando um dicionário que associa a letra da peça à função;
5. Se o movimento for legal, troca o turno. Caso contrário, exibe uma mensagem e o mesmo jogador joga de novo.

## testes.py

Reúne os testes automatizados das regras do jogo. Casos sugeridos:

- Movimentos válidos e inválidos de cada peça;
- Bloqueio de caminho para torre, bispo e dama;
- Captura de peça adversária (permitida) e da própria cor (proibida);
- Avanço duplo do peão (apenas na linha inicial);
- Alternância de turnos.

Exemplo:

```python
import tabuleiro
import pecas_linha
import capturas

def test_torre_caminho_bloqueado():
   tab = tabuleiro.criar_tabuleiro()
   # torre branca em (8,1) tentando subir: peão branco bloqueia
   assert pecas_linha.movimento_torre(8, 1, 5, 1, tab) is False

def test_cavalo_move_em_L():
   tab = tabuleiro.criar_tabuleiro()
   assert capturas.movimento_cavalo(8, 2, 6, 3, tab) is True
```

Para executar (com `pytest` instalado):

```bash
pytest testes.py
```

---

## LIMITAÇÕES CONHECIDAS

- Não há detecção de **xeque** e **xeque-mate**, então o rei pode ser capturado;
- Ainda não existem **roque**, **en passant** e **promoção do peão**;
- Não há detecção de empate (afogamento, repetição de posição etc.).

Esses itens são boas metas para as próximas versões do projeto.
