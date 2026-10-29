# Atividade Prática — Pedidos da Lanchonete

**Objetivo:** praticar a escrita de testes e o TDD, encontrando bugs e implementando novos requisitos.

O projeto simula os pedidos de uma lanchonete em Python. A classe `Pedido` calcula subtotal, frete grátis, desconto e o item mais caro e o mais barato. O código roda sem erros, mas **tem 4 bugs escondidos**.

---

## Passo a passo

1. **Faça um fork** deste repositório para a sua conta do GitHub e clone o **seu fork**.

2. **Encontre os bugs.** O código possui 4 bugs escondidos. Escreva um teste para cada um, comprovando o erro **antes** de corrigir.

3. **Corrija o código.** Depois de identificar os 4 bugs, corrija-os e confirme que todos os testes passam.

4. **Implemente 3 novos requisitos com TDD.** Siga o ciclo Red → Green → Refactor (teste antes do código) para implementar:
   - contagem de pedidos com frete grátis em uma lista;
   - situação do pedido considerando os itens sem estoque;
   - sugestão de frete grátis por SMS, simulando o serviço externo com Mock.

5. **Faça um commit após cada modificação** do código, para documentar o andamento da atividade.

6. **Entregue.** Envie o push para o seu fork e mande o link do repositório.

Os detalhes de cada passo estão logo abaixo.

---

## Regras

- Siga o ciclo TDD: escreva o teste **antes** do código.
- Um commit por passo: o histórico precisa mostrar o teste chegando antes da correção ou da implementação.
- Não altere o `src/pedido/pedido.py` antes de ter os 4 testes de bug falhando.

---

## 1. Configuração do ambiente

```bash/

python -m venv .venv
source .venv/bin/activate      # Linux/Mac
.venv\Scripts\activate         # Windows

pip install -r requirements.txt
pytest
```

O `pytest` deve mostrar **1 passed**: é o teste de exemplo que já vem pronto.

---

## 2. Estrutura do projeto

```
├── src/
│   └── pedido/
│       └── pedido.py        ← código com 4 bugs (não altere ainda)
├── tests/
│   ├── conftest.py          ← fixtures prontas
│   └── unit/
│       └── test_pedido.py   ← todos os seus testes ficam aqui
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```

---

## 3. O que o código deveria fazer

Um pedido tem um cliente e uma lista de itens. Cada `Item` tem nome, preço unitário e quantidade.

```python
from pedido.pedido import Item, Pedido

pedido = Pedido("Carla", [Item("Suco", 8.0, 2), Item("Coxinha", 6.5, 1)])
```

Comportamento **esperado** de cada método (o código atual não cumpre tudo isso):

| Método | Deve retornar |
| --- | --- |
| `quantidade_total()` | A soma das quantidades de todos os itens |
| `subtotal()` | A soma de **preço × quantidade** de todos os itens |
| `tem_frete_gratis()` | `True` se o subtotal for **a partir de R$ 50,00** (50,00 inclusive); senão, `False` |
| `item_mais_caro()` | O item com o maior preço unitário |
| `item_mais_barato()` | O item com o menor preço unitário |
| `total_com_desconto(percentual)` | O subtotal **menos** o desconto percentual. Ex.: R$ 100,00 com 10% → `90.0` |

---

## 4. Fixtures disponíveis

O `conftest.py` já tem dois pedidos prontos. Basta colocar o nome da fixture como parâmetro do teste:

```python
def test_algo(pedido_pequeno):   # Bruno: 1 café (6,00) + 2 pães de queijo (4,50 cada)
    ...

def test_outro(pedido_grande):   # Ana: 2 X-burguer (22,00) + 2 refrigerantes (7,00) + 1 batata (15,00)
    ...
```

Você também pode (e deve) criar seus próprios pedidos dentro dos testes.

---

## 5. Commits: um por passo

O histórico de commits faz parte da avaliação: ele mostra que o teste veio **antes** do código.

| Prefixo | Quando usar | Exemplo |
| --- | --- | --- |
| `test:` | Teste novo, que falha (Red) | `test: bug 1 - <o que o teste mostra>` |
| `fix:` | Correção de um bug | `fix: bug 1 - <o que foi corrigido>` |
| `feat:` | Código que faz um teste passar (Green) | `feat: requisito 1 - conta pedidos com frete grátis` |
| `refactor:` | Melhoria sem mudar o comportamento | `refactor: requisito 2 - extrai limite para constante` |

```bash
pytest
git add .
git commit -m "test: requisito 1 - lista vazia retorna zero"
```

---

## PARTE 1 — Encontre e corrija os bugs

### 1a. Escreva os testes (sem alterar o `pedido.py`)

1. Escolha um método da tabela da seção 3.
2. Calcule **à mão** o resultado esperado para um pedido.
3. Escreva o teste e rode o `pytest`.
   - **Falhou?** Você achou um bug. Faça o commit `test: bug N - ...`.
   - **Passou?** O caso não pega o erro. Tente outros valores antes de concluir que o método está certo; pense em valores-limite.
4. Repita até ter **4 testes falhando**, um por bug, e **4 commits** `test:`.

### 1b. Corrija o código

1. Corrija **um bug por vez** no `src/pedido/pedido.py`.
2. Rode `pytest` e faça o commit `fix: bug N - ...`.
3. No fim, todos os testes passam e há **4 commits** `fix:`.

> A Parte 2 usa os métodos da Parte 1. Só comece os requisitos com a Parte 1 toda verde.

---

## PARTE 2 — Três requisitos novos com TDD

> **Regra do TDD:** o teste vem **antes** do código.
>
> ```
> 🔴 RED      → escreva UM caso de teste e veja ele FALHAR
> 🟢 GREEN    → escreva o mínimo de código para passar
> 🟡 REFACTOR → melhore o código sem quebrar os testes
> ```
>
> **Nunca pule o RED.** Se o teste passou sem você escrever o código, o teste está errado.

Faça pelo menos um commit `test:` e um `feat:` por requisito; o ideal é um par por caso de teste. Use **exatamente** os nomes e textos abaixo.

### Requisito 1 — Contar pedidos com frete grátis

Uma **função** (fora da classe), em `src/pedido/pedido.py`:

```python
def contar_frete_gratis(pedidos: list) -> int
```

Recebe uma lista de pedidos e retorna quantos têm frete grátis.

**Casos que você deve testar:**

- [ ] Todos os pedidos com frete grátis
- [ ] Nenhum pedido com frete grátis
- [ ] Lista mista
- [ ] Lista vazia (retorna `0`)

> Ao importar `contar_frete_gratis` antes de ela existir, o `pytest` para com `ImportError` e nenhum teste roda. Isso é o RED. Crie a função vazia e rode de novo para ver o teste falhar pelo valor.

### Requisito 2 — Situação do pedido considerando o estoque

Um **método** da classe `Pedido`:

```python
def situacao(self, unidades_indisponiveis: int) -> str
```

A cozinha informa quantas unidades do pedido estão sem estoque. Verifique **nesta ordem**:

1. Se o percentual de unidades indisponíveis (`unidades_indisponiveis / quantidade_total()`) for **maior que 25%** → `"Cancelado por falta de estoque"`, mesmo que o pedido tenha frete grátis.
2. Senão, se o pedido tiver frete grátis → `"Confirmado com frete grátis"`.
3. Senão → `"Confirmado"`.

> Atenção: a regra é **maior que** 25%, não "maior ou igual". Com exatamente 25%, o pedido **não** é cancelado; a verificação segue para o frete. Dica: um pedido com 4 unidades e 1 indisponível tem exatamente 25%.

**Casos que você deve testar:**

- [ ] Mais de 25% indisponível em um pedido com frete grátis → `"Cancelado por falta de estoque"`
- [ ] Tudo disponível e subtotal a partir de R$ 50 → `"Confirmado com frete grátis"`
- [ ] Tudo disponível e subtotal abaixo de R$ 50 → `"Confirmado"`
- [ ] Exatamente 25% indisponível → segue para a regra do frete
- [ ] Pouco acima de 25% → `"Cancelado por falta de estoque"`

### Antes do Requisito 3: o que é Mock

Alguns códigos conversam com o mundo de fora: enviam SMS ou e-mail, cobram um cartão, chamam uma API. Nos testes, isso não pode acontecer de verdade. Ninguém quer mandar uma mensagem para um cliente real a cada `pytest`, e o teste ficaria lento e dependente da internet.

A solução é um **Mock**: um objeto **falso** que fica no lugar do serviço real. Ele não envia nada, mas **registra cada chamada** que recebe. Depois, o teste pergunta ao Mock: "você foi chamado? com quais valores?"

**Como o Mock entra no código.** O método recebe o serviço como **parâmetro**, em vez de criá-lo lá dentro. No sistema real, passa-se o serviço verdadeiro; no teste, passa-se o Mock. O código não percebe a diferença.

**Exemplo** (fora do projeto, só para entender a ideia): um cliente recebe uma mensagem de parabéns apenas no dia do aniversário.

```python
class Cliente:
    def __init__(self, nome, aniversario):
        self.nome = nome
        self.aniversario = aniversario  # "dia/mês", ex.: "05/11"

    def parabenizar(self, hoje, mensageiro):
        if hoje == self.aniversario:
            mensageiro.enviar(self.nome, "Feliz aniversário!")
```

No sistema real, a chamada seria algo como `cliente.parabenizar(hoje, ServicoDeWhatsApp())`. Nos testes, o `ServicoDeWhatsApp` é trocado por um `MagicMock`:

```python
from unittest.mock import MagicMock


def test_envia_parabens_no_aniversario():
    mensageiro = MagicMock()                    # 1. cria o mensageiro falso
    cliente = Cliente("Carla", "05/11")

    cliente.parabenizar("05/11", mensageiro)    # 2. o código usa o falso

    mensageiro.enviar.assert_called_once_with("Carla", "Feliz aniversário!")  # 3. confere


def test_nao_envia_fora_do_aniversario():
    mensageiro = MagicMock()
    cliente = Cliente("Carla", "05/11")

    cliente.parabenizar("06/11", mensageiro)

    mensageiro.enviar.assert_not_called()
```

Repare na ordem: **primeiro** o código usa o Mock, **depois** o teste confere o que aconteceu. O `MagicMock` aceita qualquer método (`enviar`, `mandar`, `disparar`...) sem você precisar criá-lo antes.

Verificações mais usadas:

| Verificação | Passa quando |
| --- | --- |
| `mock.enviar.assert_called_once_with(a, b)` | `enviar` foi chamado exatamente uma vez, com os argumentos `a` e `b` |
| `mock.enviar.assert_not_called()` | `enviar` não foi chamado nenhuma vez |
| `assert mock.enviar.call_count == 2` | `enviar` foi chamado exatamente 2 vezes |


### Requisito 3 — Sugestão de frete grátis por SMS (com Mock)

Um **método** da classe `Pedido`:

```python
def sugerir_frete_gratis(self, sms_service) -> None
```

**Regras:**

- Se o pedido **não** tiver frete grátis, chame `sms_service.enviar(cliente, valor_faltante)`, em que `valor_faltante` é quanto falta para chegar a R$ 50,00, em reais e centavos. Ex.: subtotal R$ 15,00 → `enviar("Bruno", 35.0)`.
- Se o pedido **tiver** frete grátis, o serviço **não** deve ser chamado de forma alguma.

O serviço de SMS é externo, então nos testes ele deve ser um `MagicMock` (já importado no `test_pedido.py`). Veja a seção anterior, "Antes do Requisito 3: o que é Mock".

**Casos que você deve testar:**

- [ ] Pedido abaixo de R$ 50 aciona o serviço, com o nome do cliente e o valor que falta
- [ ] Pedido acima de R$ 50 não aciona o serviço
- [ ] Pedido de exatamente R$ 50 não aciona o serviço

---

## Entrega

**Antes de enviar, confira:**

- [ ] `pytest -v` mostra todos os testes passando
- [ ] Cada um dos 4 bugs tem um teste próprio
- [ ] Os 12 casos obrigatórios da Parte 2 estão testados
- [ ] O histórico mostra cada teste antes do código correspondente
- [ ] O fork é público e o push foi feito
