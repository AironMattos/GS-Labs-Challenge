from django.test import TestCase

from ..forms import ProdutoForm

class ProdutoFormTestCase(TestCase):

    def test_produto_form_valido(self):
        form = ProdutoForm(data={
            'nome': 'Produto Teste',
            'descricao': 'Desc teste',
            'valor': 47.01

        })
        self.assertTrue(form.is_valid())
    

    def test_produto_form_invalido(self):
        form = ProdutoForm(data={})
        self.assertFalse(form.is_valid())