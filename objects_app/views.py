from django.shortcuts import render
from django.urls.conf import include

from .models import Item
from .serializers import ItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class ItemListView(APIView):
    def get(self,request,format = None):
        snippets = Item.objects.all()
        serializer =ItemSerializer(snippets ,many = True)
        return Response(serializer.data)

    
    def post(self, request):
        fool = request.data.get('fool')
        seralizer = ItemSerializer(data=fool)
        if seralizer.is_valid(raise_exception=True):
            fool_saved = seralizer.save()

        return Response({"success": "fool '{}' created successfully".format(fool_saved)})


class ItemDetailView(APIView):
    def get_object(self,pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self,request,pk,format = None):
        snippet = self.get_object(pk)
        serializer = ItemSerializer(snippet)
        return Response (serializer.data)

    def put(self,request,pk,format=None):
        snippet=self.get_object(pk)
        serializer = ItemSerializer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format= None):
        snippet=self.get_object(pk)
        snippet.delete()

    