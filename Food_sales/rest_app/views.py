from django.shortcuts import render,HttpResponse
import pandas as pd
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from . models import Food_Sales
from .serializer import Serializers_Food_Sales
def push_data_into_database(request):
    db_count=Food_Sales.objects.count()
    if request.method=="POST":
        file=request.FILES["file"]
        df = pd.read_excel(file)
        print(df.head())
        # Loop through each row in the data frame
        OrderDate=list(df["OrderDate"])
        region=list(df["Region"])
        City=list(df["City"])
        Category=list(df["Category"])
        Product=list(df["Product"])
        Quantity=list(df["Quantity"])
        UnitPrice=list(df["UnitPrice"])
        if len(df)>db_count:
            
            for i in range(len(OrderDate)):
                if not Food_Sales.objects.filter(date=OrderDate[i]):
                    Food_Sales.objects.create(date=OrderDate[i],Region=region[i],City=City[i],Category=Category[i],Product=Product[i],Quantity=Quantity[i],UnitPrice=UnitPrice[i])   
        return HttpResponse("Sucess full Dup data")
    return render(request,"index.html")
@api_view(["GET"])
def food_sales_data(request):
    page_size = 2
    page_size_query_param = 'page_size'
    pagination_class = PageNumberPagination
    pagination_class.page_size = 5
    if request.method == 'GET':
        snippets = Food_Sales.objects.all()
        serializer = Serializers_Food_Sales(snippets, many=True)

        results = Food_Sales.objects.all()
        page = pagination_class().paginate_queryset(results, request)
        serializer = Serializers_Food_Sales(page, many=True)
        # return pagination_class().get_paginated_response(serializer.data)
        return Response({"status":"Success","results":serializer.data})


