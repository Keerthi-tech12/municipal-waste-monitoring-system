from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import Zone
from .forms import ZoneForm


@login_required(login_url='/login/')
def zone_list(request):

    zones = Zone.objects.all()

    return render(
        request,
        'zone_list.html',
        {
            'zones': zones
        }
    )


@login_required(login_url='/login/')
def add_zone(request):

    success = False

    if request.method == 'POST':

        form = ZoneForm(request.POST)

        if form.is_valid():

            form.save()

            success = True

            form = ZoneForm()

    else:

        form = ZoneForm()

    return render(
        request,
        'zone_form.html',
        {
            'form': form,
            'success': success
        }
    )


@login_required(login_url='/login/')
def edit_zone(request, id):

    zone = get_object_or_404(
        Zone,
        id=id
    )

    if request.method == 'POST':

        form = ZoneForm(
            request.POST,
            instance=zone
        )

        if form.is_valid():

            form.save()

            return redirect(
                'zone_list'
            )

    else:

        form = ZoneForm(
            instance=zone
        )

    return render(
        request,
        'edit_zone.html',
        {
            'form': form
        }
    )


@login_required(login_url='/login/')
def delete_zone(request, id):

    zone = get_object_or_404(
        Zone,
        id=id
    )

    zone.delete()

    return redirect(
        'zone_list'
    )