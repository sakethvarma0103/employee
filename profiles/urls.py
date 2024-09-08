from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="all"),
    path("add",views.add,name="add"),
    path("search",views.search,name="search"),
    path("delete",views.delete,name="delete"),
    path("<slug:slug>",views.detail,name="detail"),
    path("delete/<slug:slug>",views.deleteslug,name="deleteslug"),
    path("<slug:slug>/edit",views.edit,name="edit")
]
