from django.urls import path
from .views import (
    test_api,
    get_records,
    update_record_status,
    dashboard_stats
)

from .upload_views import (
    upload_sap_csv,
    upload_utility_csv,
    upload_travel_csv,
)

urlpatterns = [
    path('test/', test_api),

    path('records/', get_records),

    path(
        'records/<int:record_id>/status/',
        update_record_status
    ),

    path('upload/sap/', upload_sap_csv),

    path('upload/utility/', upload_utility_csv),

    path('upload/travel/', upload_travel_csv),

    path('stats/', dashboard_stats),
]