from django.shortcuts import redirect, render
from .models import Produto
from .forms import ProdutoForm

# Create your views here.

def home(request):
    produtos = Produto.objects.all()

    search = request.GET.get('search')
    if search:
        produtos: Produto.objects.filter(title__icontains=search)

    context = {'produtos': produtos}
    return render(request, 'home.html', context)


def create_product(request):
    form = ProdutoForm()

    if request.method == "POST":
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    

    context = {'form':form}

    return render(request, 'create.html', context)


def delete_product(request, pk):
    produto = Produto.objects.get(id=pk)

    if request.method == "POST":
        produto.delete()
        return redirect('home')

    context = {'produto': produto}
    return render(request, 'delete.html', context)


def update_product(request, pk):
    produto = Produto.objects.get(id=pk)
    form = ProdutoForm(instance=produto)

    if request.method == "POST":
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
        return redirect('home')


    context = {'form': form}
    return render(request, 'update.html', context)


def login(request):
    return render(request,'login.html')