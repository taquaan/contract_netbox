from django.urls import path
from . import models, views
from netbox.views.generic import ObjectChangeLogView

urlpatterns = (
    # CONTRACT
    path('contracts/', views.ContractListView.as_view(), name='contract_list'),
    path('contracts/add/', views.ContractEditView.as_view(), name='contract_add'),
    path('contracts/<int:pk>/', views.ContractView.as_view(), name='contract'),
    path('contracts/<int:pk>/edit/', views.ContractEditView.as_view(), name='contract_edit'),
    path('contracts/<int:pk>/delete/', views.ContractDeleteView.as_view(), name='contract_delete'),
    path('contracts/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='contract_changelog', kwargs={
        'model': models.Contract
    }),

    # PROVIDER
    path('suppliers/', views.SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/add/', views.SupplierEditView.as_view(), name='supplier_add'),
    path('suppliers/<int:pk>/', views.SupplierView.as_view(), name='supplier'),
    path('suppliers/<int:pk>/edit/', views.SupplierEditView.as_view(), name='supplier_edit'),
    path('suppliers/<int:pk>/delete/', views.SupplierDeleteView.as_view(), name='supplier_delete'),
    path('suppliers/<int:pk>/changelog/', ObjectChangeLogView.as_view(), name='supplier_changelog', kwargs={
        'model': models.Supplier
    }),
    
    # ADD DEVICES TO CONTRACT
    path('contracts/<int:contract_id>/add-device/', views.add_devices_to_contract, name='add_device_to_contract'),
)