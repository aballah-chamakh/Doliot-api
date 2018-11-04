from django.urls import path
from .views import SimpleDocumentationListView,DocumentationRetrieveView


urlpatterns = [
    path('documentation/', SimpleDocumentationListView.as_view()),
    path('documentation/<slug:slug>/',DocumentationRetrieveView.as_view())
]
