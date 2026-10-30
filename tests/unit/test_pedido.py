import pytest
from unittest.mock import MagicMock
from pedido.pedido import Item, Pedido


# =============================================================
# EXEMPLO — um teste pronto, para você copiar o formato
# =============================================================

def test_exemplo_quantidade_total(pedido_pequeno):
    # 1 café + 2 pães de queijo = 3 unidades
    assert pedido_pequeno.quantidade_total() == 3


# =============================================================
# PARTE 1 — Encontre os bugs
# Escreva um teste para cada bug. Cada teste deve FALHAR
# no código original. Não altere src/pedido/pedido.py ainda.
# =============================================================

def test_item_mais_barato_diferente_de_mais_caro(pedido_pequeno):
    assert pedido_pequeno.item_mais_barato() != pedido_pequeno.item_mais_caro() 

def test_subtotal_com_quantidades_variadas(pedido_pequeno):
    valor_total = 0
    for item in pedido_pequeno.itens:
        valor_total += item.preco * item.quantidade
    assert valor_total == pedido_pequeno.subtotal()

def test_desconto_correto(pedido_pequeno):
    percentual = 10
    descontado = pedido_pequeno.subtotal() * (100 - percentual) / 100
    assert pedido_pequeno.total_com_desconto(10) == descontado

def test_desconto_indevido(pedido_grande):
    assert pedido_grande.tem_frete_gratis() == True


# =============================================================
# PARTE 2 — Implemente com TDD
# Siga o ciclo: 🔴 escreva o teste → 🟢 implemente → 🟡 refatore
# =============================================================

# Requisito 1 — contar_frete_gratis(pedidos) -> int
# Escreva os testes ANTES de implementar a função



# Requisito 2 — situacao(unidades_indisponiveis) -> str
# Escreva os testes ANTES de implementar o método



# Requisito 3 — sugerir_frete_gratis(sms_service) -> None
# Use MagicMock para simular o serviço de SMS
# Escreva os testes ANTES de implementar o método
