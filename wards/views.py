from django.contrib.auth.decorators import login_required
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from .models import Ward
from .forms import WardForm


@login_required(login_url='/login/')
def ward_list(request):

    wards = (
        Ward.objects
        .select_related('zone')
        .all()
    )

    return render(
        request,
        'ward_list.html',
        {
            'wards': wards
        }
    )


@login_required(login_url='/login/')
def add_ward(request):

    success = False

    if request.method == 'POST':

        form = WardForm(request.POST)

        if form.is_valid():

            form.save()

            success = True

            form = WardForm()

    else:

        form = WardForm()

    return render(
        request,
        'ward_form.html',
        {
            'form': form,
            'success': success
        }
    )


@login_required(login_url='/login/')
def edit_ward(request, id):

    ward = get_object_or_404(
        Ward,
        id=id
    )

    if request.method == 'POST':

        form = WardForm(
            request.POST,
            instance=ward
        )

        if form.is_valid():

            form.save()

            return redirect(
                'ward_list'
            )

    else:

        form = WardForm(
            instance=ward
        )

    return render(
        request,
        'edit_ward.html',
        {
            'form': form
        }
    )


@login_required(login_url='/login/')
def delete_ward(request, id):

    ward = get_object_or_404(
        Ward,
        id=id
    )

    ward.delete()

    return redirect(
        'ward_list'
    )