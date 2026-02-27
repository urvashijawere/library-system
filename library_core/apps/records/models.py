from django.db import models

class IssueRecord(models.Model):
    """
    Tracks book issue transaction
    TODO: Validator add for input records addition
    """
    class Meta:
        permissions = [
            ("can_borrow_book", "Can borrow book"),
        ]

    class IssueStatus(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        RETURNED = "RETURNED", "Returned"
        OVERDUE = "OVERDUE", "Overdue"

    book_copy = models.ForeignKey("books.BookCopy",on_delete=models.PROTECT,related_name="issue_records")
    member = models.ForeignKey("users.MemberProfile",on_delete=models.PROTECT,related_name="issues")
    issued_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    returned_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=IssueStatus.choices, default=IssueStatus.ACTIVE, db_index=True)
    fine_amount = models.DecimalField(max_digits=8, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.member.user.username} borrowed {self.book_copy}"
