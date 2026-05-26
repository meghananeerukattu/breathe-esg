from django.contrib import admin

from .models import (
    Tenant,
    DataSource,
    UploadBatch,
    RawRecord,
    NormalizedRecord,
    AuditLog
)

admin.site.register(Tenant)
admin.site.register(DataSource)
admin.site.register(UploadBatch)
admin.site.register(RawRecord)
admin.site.register(NormalizedRecord)
admin.site.register(AuditLog)