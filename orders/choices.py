from django.db import models

class OrderStatus(models.TextChoices):
    pending = "pending", "Pending"
    cancelled = "cancelled", "Cancelled"
    completed = "completed", "Completed"