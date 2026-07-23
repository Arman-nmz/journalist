# from django.http import Http404
# from django.shortcuts import render
# from rest_framework import viewsets
# from journal.models import Trade
# from journal.serializers import TradeSerializer
# from rest_framework.views import APIView
# # Create your views here.

# class TradeDetailAV(APIView):
    
#     def get_object(self, pk):
#         try:
#             return Trade.objects.get(pk = pk)    
#         except Trade.DoesNotExist:
#             raise Http404

