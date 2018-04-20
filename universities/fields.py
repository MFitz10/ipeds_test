from rest_framework import serializers

class CustomChoiceField(serializers.ChoiceField):
    """
    Serialize choice field into human-readable value of the field
    """
    def to_representation(self, value):
        if value in ('', None):
            return value
        return dict(self.choices)[value]
