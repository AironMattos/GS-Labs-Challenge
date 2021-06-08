from django.test import TestCase

from ..models import Produto


class ProdutoTestCase(TestCase):
    def setUp(self):
        Produto.objects.create(
            nome = 'Produto Teste',
            descricao = 'Descrição teste',
            valor = 38
        )
    

    def test_return_str(self):
        p1 = Produto.objects.get(nome='Produto Teste')
        self.assertEquals(p1.__str__(), ' Testando Erro')