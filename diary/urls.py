from django.urls import path
from .views import IndexView, DiaryCreateView, DiaryCreateCompleteView, DiaryListView, DiaryDetailView, DiaryUpdateView, DiaryDeleteView

app_name = 'diary'
urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('diary/create/', DiaryCreateView.as_view(), name='diary_create'),
    path('diary/create/complete/', DiaryCreateCompleteView.as_view(), name='diary_create_complete'),
    path('diary/list/', DiaryListView.as_view(), name='diary_list'),
    path('diary/detail/<uuid:pk>/', DiaryDetailView.as_view(), name='diary_detail'),
    path('diary/update/<uuid:pk>/', DiaryUpdateView.as_view(), name='diary_update'),
    path('diary/delete/<uuid:pk>/', DiaryDeleteView.as_view(), name='diary_delete'),
]