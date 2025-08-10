from django.urls import path

from .views import BookListView, BookDetailView

urlpatterns = [
    # path('myview/', MyAPIView.as_view(), name='my-view'),
    path('', BookListView.as_view()),
    path('<int:pk>/', BookDetailView.as_view()),
]