
from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view()),
    path('<int:pk>/', views.PostDetailView.as_view())
]