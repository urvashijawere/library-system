from django.core.exceptions import ValidationError


def validate_id_proof_file(value):
    """
    Max size is kept as 2MB
    """
    max_size = 2 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError(f"File too large. Max size is {max_size / (1024 * 1024)} MB.")

    valid_extensions = ('.jpg', '.jpeg', '.png', '.pdf')
    if not value.name.lower().endswith(valid_extensions):
        raise ValidationError(f"Unsupported file type. Use: {', '.join(valid_extensions)}")