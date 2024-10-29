from rest_framework import serializers

from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import Contract, Supplier

class NestedContractSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:contract-api:contract-detail'
    )

    class Meta:
        model = Contract
        fields = ('id', 'url', 'display', 'name')

class ContractSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:contract-api:contract-detail'
    )
    
    class Meta:
        model = Contract
        fields = (
            'id', 'url', 'display', 'name', 'start_date', 'end_date', 
        )
        
class SupplierSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:contract-api:supplier-detail'
    )
    
    class Meta:
        model = Supplier
        fields = (
            'id', 'url', 'display', 'name', 'phone', 'email' 
        )