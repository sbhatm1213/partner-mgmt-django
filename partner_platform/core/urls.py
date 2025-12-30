from django.urls import path
from . import views

urlpatterns = [
    path("distributors/", views.distributors),
    path("distributors/<int:distributor_id>/partners/", views.partners),
    path("partners/<int:partner_id>/sync-hubspot/", views.sync_partner),
]
