from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import validate_id_proof_file


class User(AbstractUser):
    """
    Base Model for user
    """
    phone_number = models.CharField(max_length=30, null=True, blank=True)


class LibrarianProfile(models.Model):
    """
    A Librarian profile which can create, read, update,
    delete data in library system
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="librarian_profile")
    employee_id = models.CharField(max_length=50, unique=True)
    joining_date = models.DateField()

    def __str__(self):
        return f"Librarian: {self.user.username}"


class MemberProfile(models.Model):
    """
    A Member profile who can borrow books from library
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="member_profile")
    membership_id = models.CharField(max_length=50, unique=True)
    id_proof_type = models.CharField(max_length=50)
    id_proof_number = models.CharField(max_length=100)
    id_proof_document = models.FileField(upload_to="member_id_proofs/", null=True, blank=True,
                                         validators=[validate_id_proof_file])

    def __str__(self):
        return f"Member: {self.user.username}"