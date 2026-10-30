from dataclasses import dataclass

VALOR_FRETE_GRATIS = 50.0

@dataclass
class Item:
    nome: str
    preco: float
    quantidade: int = 1

class Pedido:
    def __init__(self, cliente: str, itens: list):
        self.cliente = cliente
        self.itens = itens

    def quantidade_total(self) -> int:
        return sum(item.quantidade for item in self.itens)

    def subtotal(self) -> float:
        return sum(item.preco * item.quantidade for item in self.itens)

    def tem_frete_gratis(self) -> bool:
        return self.subtotal() > VALOR_FRETE_GRATIS

    def item_mais_caro(self) -> Item:
        return max(self.itens, key=lambda item: item.preco)

    def item_mais_barato(self) -> Item:
        return min(self.itens, key=lambda item: item.preco)

    def total_com_desconto(self, percentual: float) -> float:
        return self.subtotal() * (100 - percentual) / 100

    def situacao(self, unidades_indisponiveis: int) -> str:
        if unidades_indisponiveis / self.quantidade_total() > 0.25:
            return "Cancelado por falta de estoque"
        elif self.tem_frete_gratis():
            return "Confirmado com frete grátis"
        else:
            return "Confirmado"

    def sugerir_frete_gratis(self, sms_service):
        if not self.tem_frete_gratis():
            sms_service.enviar(self.cliente, 50.0 - self.subtotal())

def contar_frete_gratis(pedidos: list[Pedido]):
    if pedidos is None: 
        return 0

    return sum(1 for pedido in pedidos if pedido.tem_frete_gratis())
