from netbox.views import generic
from dcim.models import Device
from . import models, tables, forms, filtersets

# CONTRACTS
class ContractView(generic.ObjectView):
  queryset = models.Contract.objects.all()
  devices = models.Contract.objects.filter()
  
  # GET DEVICES RELATED TO A CONTRACT
  def get_extra_context(self, request, instance):
    contract_devices = instance.devices.all()
    table = tables.ContractListSideTable(contract_devices)
    return {
      'devices_table': table,
    }
  
class ContractListView(generic.ObjectListView):
  queryset = models.Contract.objects.all()
  table = tables.ContractListTable
  filterset = filtersets.ContractFilterSet
  filterset_form = forms.SupplierFilterForm
  
class ContractEditView(generic.ObjectEditView):
  queryset = models.Contract.objects.all()
  form = forms.ContractForm
  
class ContractDeleteView(generic.ObjectDeleteView):
  queryset = models.Contract.objects.all()

# SUPPLIERS
class SupplierView(generic.ObjectView):
  queryset = models.Supplier.objects.all()
  
  def get_extra_context(self, request, instance):
    contracts = models.Contract.objects.filter(supplier=instance.id)
    table = tables.ContractListTable(contracts)
    table.configure(request)

    return {
        'contract_table': table,
    }
  
class SupplierListView(generic.ObjectListView):
  queryset = models.Supplier.objects.all()
  table = tables.SupplierListTable
  filterset = filtersets.SupplierFilterSet
  filterset_form = forms.SupplierFilterForm
  
class SupplierEditView(generic.ObjectEditView):
  queryset = models.Supplier.objects.all()
  form = forms.SupplierForm
  
class SupplierDeleteView(generic.ObjectDeleteView):
  queryset = models.Supplier.objects.all()