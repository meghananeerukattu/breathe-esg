from django.db import models


class Tenant(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class DataSource(models.Model):

    SOURCE_CHOICES = [
        ('SAP', 'SAP'),
        ('UTILITY', 'Utility'),
        ('TRAVEL', 'Travel'),
    ]

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_CHOICES
    )

    ingestion_method = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.source_type


class UploadBatch(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('PROCESSED', 'Processed'),
        ('FAILED', 'Failed'),
    ]

    datasource = models.ForeignKey(
        DataSource,
        on_delete=models.CASCADE
    )

    filename = models.CharField(max_length=255)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    processing_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    def __str__(self):
        return self.filename


class RawRecord(models.Model):

    upload_batch = models.ForeignKey(
        UploadBatch,
        on_delete=models.CASCADE
    )

    row_number = models.IntegerField()

    raw_data = models.JSONField()

    validation_errors = models.TextField(
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Row {self.row_number}"


class NormalizedRecord(models.Model):

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('REJECTED', 'Rejected'),
    ]

    SCOPE_CHOICES = [
        ('SCOPE_1', 'Scope 1'),
        ('SCOPE_2', 'Scope 2'),
        ('SCOPE_3', 'Scope 3'),
    ]

    raw_record = models.ForeignKey(
        RawRecord,
        on_delete=models.CASCADE
    )

    source_type = models.CharField(max_length=20)

    category = models.CharField(max_length=100)

    scope = models.CharField(
        max_length=20,
        choices=SCOPE_CHOICES
    )

    quantity = models.FloatField()

    normalized_unit = models.CharField(max_length=50)

    suspicious_flag = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='PENDING'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category


class AuditLog(models.Model):

    normalized_record = models.ForeignKey(
        NormalizedRecord,
        on_delete=models.CASCADE
    )

    action = models.CharField(max_length=100)

    old_value = models.TextField(
        blank=True,
        null=True
    )

    new_value = models.TextField(
        blank=True,
        null=True
    )

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.action
