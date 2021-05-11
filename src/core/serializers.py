from rest_framework import serializers
from .models import Quote

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = (
                "from_currency",
                "to_currency",
                )