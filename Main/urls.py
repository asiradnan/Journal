from django.urls import path
from . import views

urlpatterns = [
    path('',views.publicPosts.as_view(),name="publicposts"),
    path('create',views.create.as_view(),name="create"),
    path('update/<int:pk>/',views.update.as_view(),name="update"),
    path('delete/<int:pk>/',views.delete.as_view(),name="delete"),
]