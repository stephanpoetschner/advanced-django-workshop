from rest_framework import serializers

from jobs.models import Company


class CompanySearchSerializer(serializers.Serializer):
    term = serializers.CharField()

    def search(self, companies):
        q = self.validated_data.get('term')
        if q:
            companies = companies.filter(name__icontains=q)
        return companies


class CompanyNameSerializer(serializers.Serializer):
    id = serializers.CharField()
    text = serializers.CharField()


class CompanySerializer(serializers.Serializer):
    term = serializers.CharField(allow_blank=True)
    results = CompanyNameSerializer(many=True)
