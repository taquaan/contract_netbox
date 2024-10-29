from contract.api.serializers import ContractSerializer, SupplierSerializer
from netbox.api.viewsets import NetBoxModelViewSet
from contract import models, filtersets

class ContractViewSet(NetBoxModelViewSet):
  queryset = models.Contract.objects.prefetch_related('tenant', 'devices', 'supplier').all()
  serializer_class = ContractSerializer
  
class SupplierViewSet(NetBoxModelViewSet):
  queryset = models.Supplier.objects.all()
  serializer_class = SupplierSerializer
