from journal.api.views import TradeDetailedAV, TradeListAV
from django.urls import path

urlpatterns = [
    path('<int:pk>', TradeDetailedAV.as_view(), name='trade-detail'),
    path('list', TradeListAV.as_view(), name='trade-list'),
]
