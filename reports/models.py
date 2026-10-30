from django.db import models

class LostFoundReport(models.Model):
    class ReportType(models.TextChoices):
        LOST = 'LOST', 'Lost'
        FOUND = 'FOUND', 'Found'

    class StatusChoices(models.TextChoices):
        OPEN = 'OPEN', 'Open'
        RESOLVED = 'RESOLVED', 'Resolved'

    report_type = models.CharField(
        max_length=5, 
        choices=ReportType.choices, 
        default=ReportType.LOST, 
        help_text="Indicates whether the item was lost or found"
    )
    item_name = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    location = models.CharField(max_length=255)
    date_reported = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=10, 
        choices=StatusChoices.choices, 
        default=StatusChoices.OPEN,
    )

    def __str__(self):
        return f"{self.report_type} - {self.item_name}"
