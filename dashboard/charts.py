import matplotlib

matplotlib.use('Agg')

import matplotlib.pyplot as plt
from django.db.models import Sum, Count
from django.db.models.functions import ExtractMonth

from waste_collection.models import WasteCollection


# ==========================
# WARD BAR CHART
# ==========================

def generate_ward_chart():

    ward_data = (
        WasteCollection.objects
        .values('ward__ward_name')
        .annotate(total_waste=Sum('waste_quantity'))
        .order_by('-total_waste')
    )

    wards = []
    waste = []

    for item in ward_data:
        wards.append(item['ward__ward_name'])
        waste.append(float(item['total_waste']))

    plt.figure(figsize=(14, 7))

    bars = plt.bar(
        wards,
        waste,
        color='#0f766e'
    )

    plt.title(
        "Ward Wise Waste Collection",
        fontsize=16,
        fontweight='bold'
    )

    plt.xlabel("Ward", fontsize=12)
    plt.ylabel("Waste (kg)", fontsize=12)

    plt.grid(
        axis='y',
        linestyle='--',
        alpha=0.3
    )

    plt.xticks(rotation=20)

    for bar in bars:
        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f'{int(height)}',
            ha='center',
            va='bottom',
            fontsize=10,
            fontweight='bold'
        )

    plt.tight_layout()

    plt.savefig(
        "static/ward_chart.png",
        dpi=200,
        bbox_inches='tight'
    )

    plt.close()


# ==========================
# MONTHLY TREND CHART
# ==========================

def generate_monthly_chart():

    monthly_data = (
        WasteCollection.objects
        .annotate(month=ExtractMonth('collection_date'))
        .values('month')
        .annotate(total_waste=Sum('waste_quantity'))
        .order_by('month')
    )

    month_names = [
        "",
        "Jan", "Feb", "Mar", "Apr",
        "May", "Jun", "Jul", "Aug",
        "Sep", "Oct", "Nov", "Dec"
    ]

    months = []
    waste = []

    for item in monthly_data:
        months.append(month_names[item['month']])
        waste.append(float(item['total_waste']))

    plt.figure(figsize=(14, 7))

    plt.plot(
        months,
        waste,
        marker='o',
        markersize=10,
        linewidth=3,
        color='#2563eb'
    )

    plt.fill_between(
        months,
        waste,
        alpha=0.2
    )

    plt.title(
        "Monthly Waste Collection Trend",
        fontsize=16,
        fontweight='bold'
    )

    plt.xlabel("Month", fontsize=12)
    plt.ylabel("Waste (kg)", fontsize=12)

    plt.grid(
        linestyle='--',
        alpha=0.3
    )

    for x, y in zip(months, waste):
        plt.text(
            x,
            y,
            int(y),
            fontsize=10,
            ha='center',
            va='bottom'
        )

    plt.tight_layout()

    plt.savefig(
        "static/monthly_chart.png",
        dpi=200,
        bbox_inches='tight'
    )

    plt.close()


# ==========================
# DOUGHNUT PIE CHART
# ==========================

def generate_zone_pie_chart():

    zone_data = (
        WasteCollection.objects
        .values('ward__zone__zone_name')
        .annotate(total_waste=Sum('waste_quantity'))
    )

    zones = []
    waste = []

    for item in zone_data:
        zones.append(item['ward__zone__zone_name'])
        waste.append(float(item['total_waste']))

    if not zones:
        return

    colors = [
        '#0f766e',
        '#2563eb',
        '#7c3aed',
        '#ea580c',
        '#dc2626'
    ]

    plt.figure(figsize=(10, 10))
    plt.pie(
        waste,
        labels=zones,
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        wedgeprops={
            'width': 0.45
        }
    )

    plt.title(
        "Zone Wise Waste Distribution",
        fontsize=16,
        fontweight='bold'
    )

    plt.tight_layout()

    plt.savefig(
        "static/zone_pie_chart.png",
        dpi=200,
        bbox_inches='tight'
    )

    plt.close()

def generate_vehicle_chart():

    vehicle_data = (
        WasteCollection.objects
        .values('vehicle__vehicle_number')
        .annotate(
            total_collections=Count('id')
        )
        .order_by('-total_collections')[:5]
    )

    vehicles = []
    collections = []

    for item in vehicle_data:

        vehicles.append(
            item['vehicle__vehicle_number']
        )

        collections.append(
            item['total_collections']
        )

    if len(vehicles) == 0:
        return

    plt.figure(figsize=(10, 5))

    bars = plt.barh(
        vehicles,
        collections,
        color='#10b981',
        edgecolor='#0f766e',
        linewidth=2
    )

    plt.title(
        "Top 5 Active Vehicles",
        fontsize=18,
        fontweight='bold',
        color='#0f766e'
    )

    plt.xlabel(
        "Number of Collections",
        fontsize=12
    )

    plt.grid(
        axis='x',
        linestyle='--',
        alpha=0.3
    )

    for bar in bars:

        width = bar.get_width()

        plt.text(
            width + 0.05,
            bar.get_y() + bar.get_height()/2,
            str(int(width)),
            va='center',
            fontsize=11,
            fontweight='bold',
            color='#0f766e'
        )

    plt.tight_layout()

    plt.savefig(
        "static/vehicle_chart.png",
        dpi=300,
        bbox_inches='tight'
    )

    plt.close('all')