from django.db import models

class IssueRecord(models.Model):
    """
    Tracks book issue transaction
    """
    class IssueStatus(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        RETURNED = "RETURNED", "Returned"
        OVERDUE = "OVERDUE", "Overdue"

    book_copy = models.ForeignKey("books.BookCopy",on_delete=models.PROTECT,related_name="issue_records")
    member = models.ForeignKey("accounts.User",on_delete=models.PROTECT,related_name="issues")
    issued_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    returned_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=IssueStatus, default=IssueStatus.ACTIVE, db_index=True)
    fine_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)