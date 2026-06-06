from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Produit, Ingredient, CompositionProduit

IMAGE_MAP = {
    'Poulet DG': 'Poulet DG.PNG',
    'Ndol\u251c\u00ae': 'Ndole.PNG',
    'Riz saut\u251c\u00ae': 'Riz saute.PNG',
    'Jus de Gingembre': 'Jus de Jingembre.PNG',
    'Jus de Bissap': 'Jus de Bissap.PNG',
}

@login_required
def product_list(request):
    products = Produit.objects.all()
    for p in products:
        p.img_file = IMAGE_MAP.get(p.nom, '')
    return render(request, 'products/list.html', {'products': products})

@login_required
def product_create(request):
    if request.method == 'POST':
        produit = Produit.objects.create(
            nom=request.POST['nom'],
            description=request.POST['description'],
            duree_cuisson=request.POST['duree_cuisson'],
            nombre_personnes=request.POST['nombre_personnes'],
        )
        messages.success(request, 'Product created successfully!')
        return redirect('products:list')
    return render(request, 'products/create.html')
