from django.shortcuts import render

# Create your views here.

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import NormalizedRecord
from .serializers import NormalizedRecordSerializer


@api_view(['GET'])
def test_api(request):
    return Response({
        "message": "Backend working successfully"
    })


@api_view(['GET'])
def get_records(request):

    records = NormalizedRecord.objects.all().order_by('-id')

    serializer = NormalizedRecordSerializer(records, many=True)

    return Response(serializer.data)
@api_view(['POST'])
def update_record_status(request, record_id):



    try:
        record = NormalizedRecord.objects.get(id=record_id)

    except NormalizedRecord.DoesNotExist:

        return Response({
            "error": "Record not found"
        }, status=404)

    status_value = request.data.get('status')

    if status_value not in ['APPROVED', 'REJECTED']:

        return Response({
            "error": "Invalid status"
        }, status=400)

    record.status = status_value

    record.save()

    return Response({
        "message": f"Record marked as {status_value}"
    })
@api_view(['GET'])
def dashboard_stats(request):

    total_records = NormalizedRecord.objects.count()

    suspicious_records = NormalizedRecord.objects.filter(
        suspicious_flag=True
    ).count()

    approved_records = NormalizedRecord.objects.filter(
        status='APPROVED'
    ).count()

    return Response({
        "total_records": total_records,
        "suspicious_records": suspicious_records,
        "approved_records": approved_records
    })