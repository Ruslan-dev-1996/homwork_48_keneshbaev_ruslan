from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import ProductForm
from webapp.models import Product, PRODUCT_OTHER_CHOICE



def index_view(request, *args, **kwargs):
    search_query = request.GET.get('search', '')
    products = Product.objects.filter(amount__gt=0).order_by('category')
    if search_query:
        products = Product.objects.filter(name__icontains=search_query, amount__gt=0)
        return render(request, 'index.html', context={

        'products':products})
    else:
        return render(request, 'index.html', context={
        'products': products
    })

def detailed_view(request, pk):
    task = get_object_or_404(Product, pk=pk)
    return render(request, 'detailed.html', context={
       'task': task
    })
def form_storage_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'form.html', context={
            'form': form,
            'status_choices': PRODUCT_OTHER_CHOICE
        })
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)

        if not form.is_valid():
            return render(request, 'form.html', context={'form': form, 'status_choices': PRODUCT_OTHER_CHOICE})

        Product.objects.create(
            name=form.cleaned_data['name'],
            description=form.cleaned_data['description'],
            category=form.cleaned_data['category'],
            amount=form.cleaned_data['amount'],
            price=form.cleaned_data['price']

        )
        return redirect('index')



def detailed_update_view(request, pk):
    task = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(data={
            'name': task.name,
            'description': task.description,
            'category': task.category,
            'amunt': task.amount,
            'price': task.price
        })
        return render(request, 'update.html', context={'form': form, 'task': task})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            task.name = form.cleaned_data['name']
            task.description = form.cleaned_data['description']
            task.category = form.cleaned_data['category']
            task.amount = form.cleaned_data['amount']
            task.price = form.cleaned_data['price']
            task.save()
            return redirect('detailed', pk=task.pk)

        return render(request, 'update.html', context={'form': form, 'task': task})



def detailed_delete_view(request, pk):
    task = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
       return render(request, 'delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')
