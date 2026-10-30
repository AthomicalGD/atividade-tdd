import pytest
from pedido.pedido import Item, Pedido

@pytest.fixture
def pedido_pequeno():
    return Pedido(
        cliente="Bruno",
        itens=[
            Item("Café", 6.0, 1),
            Item("Pão de queijo", 4.5, 2),
        ],
    )

@pytest.fixture
def pedido_grande():
    return Pedido(
        cliente="Ana",
        itens=[
            Item("X-burguer", 22.0, 2),
            Item("Refrigerante", 7.0, 2),
            Item("Batata frita", 15.0, 1),
        ],
    )

@pytest.fixture
def pedidos_mistos():
    return [
        Pedido(
            cliente="Ana",
            itens=[
                Item("X-burguer", 22.0, 2),
                Item("Refrigerante", 7.0, 2),
                Item("Batata frita", 15.0, 1),
            ]),
        Pedido(
            cliente="Bruno",
            itens=[
                Item("Café", 6.0, 1),
                Item("Pão de queijo", 4.5, 2),
            ],
        )
    ]

@pytest.fixture
def pedidos_vazio():
    return

@pytest.fixture
def pedidos_sem_frete():
    return [
        Pedido(
            cliente="Carlos",
            itens=[
                Item("Café", 6.0, 1),
                Item("Churros", 10.0, 2)
            ]
        ),
        Pedido(
            cliente="Jonathan",
            itens=[
                Item("Refrigerante", 7.0, 3),
                Item("Brotinho", 28.0, 1)
            ]
        )
    ]

@pytest.fixture
def pedidos_com_frete():
    return [
        Pedido(
            cliente="Carlos",
            itens=[
                Item("Chocolate", 8.0, 1),
                Item("Churros", 11.0, 3),
                Item("Cappuccino", 12.0, 1)
            ]
        ),
        Pedido(
            cliente="Emília",
            itens=[
                Item("Bolo", 40.0, 1),
                Item("Crepe", 35.0, 1)
            ]
        )
    ]