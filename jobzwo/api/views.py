from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import views

from jobs.models import Company

from .serializers import CompanySerializer, CompanySearchSerializer


class CompanyView(views.APIView):
    def get(self, request):
        companies = Company.objects.all()

        term = ''
        search_serializer = CompanySearchSerializer(data=request.query_params)
        if search_serializer.is_valid():
            companies = search_serializer.search(companies)
            term = search_serializer.validated_data.get('term')

        company_names = companies.values('id', 'name') \
            .distinct().order_by('name')

        # map return objects to interface expected by select2
        company_names = map(lambda x: {
            'id': x['id'],
            'text': x['name'],
        }, company_names)

        serializer = CompanySerializer(data={
            'term': term,
            'results': list(company_names),
        })
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors,
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)
