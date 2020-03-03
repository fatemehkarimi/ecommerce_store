from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


PHONE_REGEX = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format:\
             '+999999999'. Up to 15 digits allowed.")


def profile_pic_size_limit(value):
    limit = 2 * 1024 * 1024
    message='Image is too large. Size should not exceed 2MB.'
    if value.size > limit:
        raise ValidationError('Image is too large. Size should not exceed 2MB.')