from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import WasteCollectionForm
from .models import WasteCollection
from django.core.paginator import Paginator

@login_required(login_url='/login/')
def add_waste_collection(request):

    success = False

    if request.method == 'POST':

        form = WasteCollectionForm(request.POST)

        if form.is_valid():

            form.save()

            success = True

            form = WasteCollectionForm()

    else:

        form = WasteCollectionForm()

    return render(
        request,
        'waste_collection_form.html',
        {
            'form': form,
            'success': success
        }
    )


@login_required(login_url='/login/')
def collection_history(request):

    search = request.GET.get('search')

    collections = (
        WasteCollection.objects
        .all()
        .order_by('-collection_date', '-collection_time')
    )

    if search:

        collections = collections.filter(
            ward__ward_name__icontains=search
        )

    paginator = Paginator(
        collections,
        5
    )

    page_number = request.GET.get('page')

    collections = paginator.get_page(
        page_number
    )

    return render(
        request,
        'collection_history.html',
        {
            'collections': collections,
            'search': search
        }
    )

@login_required(login_url='/login/')
def edit_collection(request, id):
    collection = get_object_or_404(
        WasteCollection,
        id=id
    )

    if request.method == 'POST':

        form = WasteCollectionForm(
            request.POST,
            instance=collection
        )

        if form.is_valid():

            form.save()

            return redirect('collection_history')

    else:

        form = WasteCollectionForm(
            instance=collection
        )

    return render(
        request,
        'edit_collection.html',
        {
            'form': form
        }
    )
@login_required(login_url='/login/')
def delete_collection(request, id):
    collection = get_object_or_404(
        WasteCollection,
        id=id
    )

    collection.delete()

    return redirect(
        'collection_history'
    )