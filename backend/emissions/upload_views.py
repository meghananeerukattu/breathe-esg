import pandas as pd

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import (
    Tenant,
    DataSource,
    UploadBatch,
    RawRecord,
    NormalizedRecord
)


@api_view(['POST'])
def upload_sap_csv(request):

    file = request.FILES.get('file')

    if not file:
        return Response({
            "error": "No file uploaded"
        }, status=400)

    # Read CSV
    df = pd.read_csv(file)

    # Create sample tenant
    tenant, _ = Tenant.objects.get_or_create(
        name="Demo Enterprise"
    )

    # Create datasource
    datasource, _ = DataSource.objects.get_or_create(
        tenant=tenant,
        source_type='SAP',
        defaults={
            'ingestion_method': 'CSV Upload'
        }
    )

    # Create upload batch
    batch = UploadBatch.objects.create(
        datasource=datasource,
        filename=file.name,
        processing_status='PROCESSED'
    )

    processed_count = 0

    for index, row in df.iterrows():

        raw_record = RawRecord.objects.create(
            upload_batch=batch,
            row_number=index + 1,
            raw_data=row.to_dict()
        )

        quantity = row.get('quantity', 0)

        suspicious = False

        if quantity < 0:
            suspicious = True

        # Normalize units
        unit = str(row.get('unit', '')).lower()

        if unit in ['litre', 'litres', 'l']:
            normalized_unit = 'L'

        elif unit in ['kg', 'kilogram']:
            normalized_unit = 'KG'

        else:
            normalized_unit = 'UNKNOWN'
            suspicious = True

        NormalizedRecord.objects.create(
            raw_record=raw_record,
            source_type='SAP',
            category=row.get('fuel_type', 'Unknown'),
            scope='SCOPE_1',
            quantity=quantity,
            normalized_unit=normalized_unit,
            suspicious_flag=suspicious
        )

        processed_count += 1

    return Response({
        "message": "SAP CSV uploaded successfully",
        "rows_processed": processed_count
    })
@api_view(['POST'])
def upload_utility_csv(request):

    file = request.FILES.get('file')

    if not file:
        return Response({
            "error": "No file uploaded"
        }, status=400)

    df = pd.read_csv(file)

    tenant, _ = Tenant.objects.get_or_create(
        name="Demo Enterprise"
    )

    datasource, _ = DataSource.objects.get_or_create(
        tenant=tenant,
        source_type='UTILITY',
        defaults={
            'ingestion_method': 'CSV Upload'
        }
    )

    batch = UploadBatch.objects.create(
        datasource=datasource,
        filename=file.name,
        processing_status='PROCESSED'
    )

    processed_count = 0

    for index, row in df.iterrows():

        raw_record = RawRecord.objects.create(
            upload_batch=batch,
            row_number=index + 1,
            raw_data=row.to_dict()
        )

        quantity = row.get('kwh_used', 0)

        suspicious = False

        if quantity < 0:
            suspicious = True

        unit = str(row.get('unit', '')).lower()

        if unit == 'kwh':
            normalized_unit = 'KWH'

        else:
            normalized_unit = 'UNKNOWN'
            suspicious = True

        NormalizedRecord.objects.create(
            raw_record=raw_record,
            source_type='UTILITY',
            category='Electricity',
            scope='SCOPE_2',
            quantity=quantity,
            normalized_unit=normalized_unit,
            suspicious_flag=suspicious
        )

        processed_count += 1

    return Response({
        "message": "Utility CSV uploaded successfully",
        "rows_processed": processed_count
    })
@api_view(['POST'])
def upload_travel_csv(request):

    file = request.FILES.get('file')

    if not file:
        return Response({
            "error": "No file uploaded"
        }, status=400)

    df = pd.read_csv(file)

    tenant, _ = Tenant.objects.get_or_create(
        name="Demo Enterprise"
    )

    datasource, _ = DataSource.objects.get_or_create(
        tenant=tenant,
        source_type='TRAVEL',
        defaults={
            'ingestion_method': 'CSV Upload'
        }
    )

    batch = UploadBatch.objects.create(
        datasource=datasource,
        filename=file.name,
        processing_status='PROCESSED'
    )

    processed_count = 0

    for index, row in df.iterrows():

        raw_record = RawRecord.objects.create(
            upload_batch=batch,
            row_number=index + 1,
            raw_data=row.to_dict()
        )

        quantity = row.get('distance', 0)

        suspicious = False

        if quantity < 0:
            suspicious = True

        unit = str(row.get('unit', '')).lower()

        if unit == 'km':
            normalized_unit = 'KM'

        elif unit == 'nights':
            normalized_unit = 'NIGHTS'

        else:
            normalized_unit = 'UNKNOWN'
            suspicious = True

        NormalizedRecord.objects.create(
            raw_record=raw_record,
            source_type='TRAVEL',
            category=row.get('trip_type', 'Travel'),
            scope='SCOPE_3',
            quantity=quantity,
            normalized_unit=normalized_unit,
            suspicious_flag=suspicious
        )

        processed_count += 1

    return Response({
        "message": "Travel CSV uploaded successfully",
        "rows_processed": processed_count
    })