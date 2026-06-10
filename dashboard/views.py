from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Sum, Avg, Count

from users.decorators import (
    commissioner_or_zone_officer
)

from .charts import (
    generate_ward_chart,
    generate_monthly_chart,
    generate_zone_pie_chart,
    generate_vehicle_chart
)

from zones.models import Zone
from wards.models import Ward
from vehicles.models import Vehicle
from waste_collection.models import WasteCollection


@login_required(login_url='/login/')
@commissioner_or_zone_officer
def dashboard(request):

    profile = request.user.userprofile

    if profile.role == 'Data Entry Operator':
        return redirect('/waste-collection/')

    # Dashboard Counts
    total_zones = Zone.objects.count()
    total_wards = Ward.objects.count()
    total_vehicles = Vehicle.objects.count()
    total_collections = WasteCollection.objects.count()

    # Total Waste
    total_waste_today = (
        WasteCollection.objects.aggregate(
            Sum('waste_quantity')
        )['waste_quantity__sum']
        or 0
    )

    # Average Waste
    average_waste = (
        WasteCollection.objects.aggregate(
            Avg('waste_quantity')
        )['waste_quantity__avg']
        or 0
    )

    # Ward Summary
    ward_summary = (
        WasteCollection.objects
        .values('ward__ward_name')
        .annotate(total_waste=Sum('waste_quantity'))
        .order_by('-total_waste')
    )

    # Zone Summary
    zone_summary = (
        WasteCollection.objects
        .values('ward__zone__zone_name')
        .annotate(total_waste=Sum('waste_quantity'))
        .order_by('-total_waste')
    )

    # Top Ward
    top_ward = ward_summary.first()

    # Top Zone
    top_zone = zone_summary.first()

    # Top 5 Wards
    top_5_wards = ward_summary[:5]

    # Vehicle Analytics
    vehicle_summary = (
        WasteCollection.objects
        .values('vehicle__vehicle_number')
        .annotate(
            total_collections=Count('id'),
            total_waste=Sum('waste_quantity')
        )
        .order_by('-total_collections')
    )

    top_vehicle = vehicle_summary.first()

    # Recent Collections
    recent_collections = (
        WasteCollection.objects
        .select_related('ward', 'vehicle')
        .order_by(
            '-collection_date',
            '-collection_time'
        )[:10]
    )

    context = {

        'total_zones': total_zones,
        'total_wards': total_wards,
        'total_vehicles': total_vehicles,
        'total_collections': total_collections,

        'total_waste_today': total_waste_today,
        'average_waste': round(
            float(average_waste),
            2
        ),

        'ward_summary': ward_summary,
        'zone_summary': zone_summary,

        'top_ward': top_ward,
        'top_zone': top_zone,
        'top_vehicle': top_vehicle,

        'top_5_wards': top_5_wards,

        'recent_collections': recent_collections,
    }

    generate_ward_chart()
    generate_monthly_chart()
    generate_zone_pie_chart()
    generate_vehicle_chart()

    return render(
        request,
        'dashboard.html',
        context
    )