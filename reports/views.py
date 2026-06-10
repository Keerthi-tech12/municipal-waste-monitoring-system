from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Sum
from django.http import HttpResponse
from django.db.models.functions import TruncMonth

import openpyxl

from waste_collection.models import WasteCollection

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle
)

from reportlab.lib import colors

from users.decorators import (
    commissioner_or_zone_officer
)


@login_required(login_url='/login/')
@commissioner_or_zone_officer
def daily_report(request):

    collections = WasteCollection.objects.all().order_by(
        '-collection_date',
        '-collection_time'
    )

    return render(
        request,
        'daily_report.html',
        {
            'collections': collections
        }
    )


@login_required(login_url='/login/')
@commissioner_or_zone_officer
def ward_report(request):

    ward_data = (
        WasteCollection.objects
        .values('ward__ward_name')
        .annotate(total_waste=Sum('waste_quantity'))
        .order_by('-total_waste')
    )

    return render(
        request,
        'ward_report.html',
        {
            'ward_data': ward_data
        }
    )


@login_required(login_url='/login/')
@commissioner_or_zone_officer
def zone_report(request):

    zone_data = (
        WasteCollection.objects
        .values('ward__zone__zone_name')
        .annotate(total_waste=Sum('waste_quantity'))
        .order_by('-total_waste')
    )

    return render(
        request,
        'zone_report.html',
        {
            'zone_data': zone_data
        }
    )


@login_required(login_url='/login/')
@commissioner_or_zone_officer
def monthly_report(request):

    monthly_data = (
        WasteCollection.objects
        .annotate(month=TruncMonth('collection_date'))
        .values('month')
        .annotate(total_waste=Sum('waste_quantity'))
        .order_by('month')
    )

    return render(
        request,
        'monthly_report.html',
        {
            'monthly_data': monthly_data
        }
    )


@login_required(login_url='/login/')
@commissioner_or_zone_officer
def export_ward_excel(request):

    ward_data = (
        WasteCollection.objects
        .values('ward__ward_name')
        .annotate(total_waste=Sum('waste_quantity'))
        .order_by('-total_waste')
    )

    workbook = openpyxl.Workbook()

    sheet = workbook.active
    sheet.title = "Ward Report"

    sheet.append([
        "Ward Name",
        "Total Waste (kg)"
    ])

    for ward in ward_data:

        sheet.append([
            ward['ward__ward_name'],
            float(ward['total_waste'])
        ])

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

    response['Content-Disposition'] = (
        'attachment; filename=ward_report.xlsx'
    )

    workbook.save(response)

    return response


@login_required(login_url='/login/')
@commissioner_or_zone_officer
def export_ward_pdf(request):

    ward_data = (
        WasteCollection.objects
        .values('ward__ward_name')
        .annotate(total_waste=Sum('waste_quantity'))
        .order_by('-total_waste')
    )

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        'attachment; filename="ward_report.pdf"'
    )

    pdf = SimpleDocTemplate(response)

    data = [
        ["Ward Name", "Total Waste (kg)"]
    ]

    for ward in ward_data:

        data.append([
            ward['ward__ward_name'],
            str(ward['total_waste'])
        ])

    table = Table(data)

    table.setStyle(TableStyle([

        (
            'BACKGROUND',
            (0, 0),
            (-1, 0),
            colors.lightblue
        ),

        (
            'GRID',
            (0, 0),
            (-1, -1),
            1,
            colors.black
        ),

        (
            'FONTNAME',
            (0, 0),
            (-1, 0),
            'Helvetica-Bold'
        ),

    ]))

    pdf.build([table])

    return response