"""
Validator for users app
"""

from django.core import validators
from django.utils.deconstruct import deconstructible


@deconstructible
class CarnetValidator(validators.RegexValidator):
    regex = r'\d{9}^$'
    message = (
        'Ingrese username váldio. Este valor debe contener '
        'el número de carnet del estudiante: Ej: 200012345'
    )
    flags = 0
