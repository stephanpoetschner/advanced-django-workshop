from rest_framework.response import Response
from rest_framework.viewsets import views

from jobs.models import Company

from .serializers import CompanyNameSerializer


class CompanyView(views.APIView):
    def get(self, request):
        companies = Company.objects.all()

        company_names = companies.values('id', 'name') \
            .distinct().order_by('name')

        # map return objects to interface expected by select2
        company_names = map(lambda x: {
            'id': x['id'],
            'text': x['name'],
        }, company_names)

        serializer = CompanyNameSerializer(company_names, many=True)

        return Response(serializer.data)
