from netbox.filtersets import NetBoxModelFilterSet
from .models import Contract, Supplier
from utilities.forms.widgets import DatePicker

class ContractFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Contract
        fields = ('id', 'name', 'status', 'devices', 'supplier', 'start_date', 'end_date', 'renewal_term', 'comments')
        widgets = {
          'start_date': DatePicker(),
          'end_date': DatePicker(),
        }
        
    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)
      
class SupplierFilterSet(NetBoxModelFilterSet):

    class Meta:
        model = Supplier
        fields = ('id', 'name', 'phone', 'email')
        
    def search(self, queryset, name, value):
        return queryset.filter(name__icontains=value)