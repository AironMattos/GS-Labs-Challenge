from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Produto

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'


    widgets ={
        'nome': TextInput(attrs={'placeholder': 'Nome do Produto'})
    }
