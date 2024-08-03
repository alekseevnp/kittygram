from django.urls import path

from cats.views import APICat  # , cat_list

urlpatterns = [
    path("cats/", APICat.as_view()),
    #   path('cats/', cat_list),
]
