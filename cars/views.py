from django.shortcuts import render, redirect, get_object_or_404
from . models import Owner, Car
from django.contrib.auth.decorators import login_required


@login_required
def owner_list(request):
    owners = Owner.objects.all()
    return render(request, 'cars/owner_list.html', {'owners': owners})


@login_required
def owner_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        owner = Owner.objects.create(name=name)
        return redirect('owner_list')
    return render(request, 'cars/owner_create.html')


@login_required
def owner_edit(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    if request.method == 'POST':
        name = request.POST['name']
        owner.name = name
        owner.save()
        return redirect('owner_list')
    return render(request, 'cars/owner_edit.html', {'owner': owner})


@login_required
def owner_delete(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    if request.method == 'POST':
        owner.delete()
        return redirect('owner_list')
    return render(request, 'cars/owner_delete.html', {'owner': owner})


@login_required
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})


@login_required
def car_create(request):
    if request.method == 'POST':
        color = request.POST['color']
        model = request.POST['model']
        owner_id = request.POST['owner']
        owner = Owner.objects.get(id=owner_id)
        car = Car.objects.create(color=color, model=model, owner=owner)
        return redirect('car_list')
    owners = Owner.objects.filter(has_car=False)
    return render(request, 'cars/car_create.html', {'owner': owners})


@login_required
def car_edit(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        color = request.POST['color']
        model = request.POST['model']
        owner_id = request.POST['owner']
        owner = Owner.objects.get(id=owner_id)
        car.color = color
        car.model = model
        car.owner = owner
        car.save()
        return redirect('car_list')
    owners = Owner.objects.all()
    return render(request, 'cars/car_edit.html', {'car': car, 'owners': owners})


@login_required
def car_delete(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'POST':
        car.delete()
        return redirect('car_list')
    return render(request, 'cars/car_delete.html', {'car': car})