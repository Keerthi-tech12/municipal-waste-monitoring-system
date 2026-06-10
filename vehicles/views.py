from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import VehicleForm
from django.shortcuts import render
from .models import Vehicle


@login_required(login_url='/login/')
def vehicle_list(request):

    vehicles = Vehicle.objects.all()

    return render(
        request,
        'vehicle_list.html',
        {
            'vehicles': vehicles
        }
    )
@login_required(login_url='/login/')
def add_vehicle(request):

    success = False

    if request.method == 'POST':

        form = VehicleForm(request.POST)

        if form.is_valid():

            form.save()

            success = True

            form = VehicleForm()

    else:

        form = VehicleForm()

    return render(
        request,
        'vehicle_form.html',
        {
            'form': form,
            'success': success
        }
    )
@login_required(login_url='/login/')
def edit_vehicle(request, id):

    vehicle = get_object_or_404(
        Vehicle,
        id=id
    )

    if request.method == 'POST':

        form = VehicleForm(
            request.POST,
            instance=vehicle
        )

        if form.is_valid():

            form.save()

            return redirect('vehicle_list')

    else:

        form = VehicleForm(
            instance=vehicle
        )

    return render(
        request,
        'edit_vehicle.html',
        {
            'form': form
        }
    )


@login_required(login_url='/login/')
def delete_vehicle(request, id):

    vehicle = get_object_or_404(
        Vehicle,
        id=id
    )

    vehicle.delete()

    return redirect(
        'vehicle_list'
    )