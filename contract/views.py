import json
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from netbox.views import generic
from dcim.models import Device, Site, DeviceRole, DeviceType
from . import models, tables, forms, filtersets

# CONTRACTS
class ContractView(generic.ObjectView):
  queryset = models.Contract.objects.all()
  devices = models.Contract.objects.filter()
  
  # GET DEVICES RELATED TO A CONTRACT
  def get_extra_context(self, request, instance):
    sites = Site.objects.all()
    roles = DeviceRole.objects.all()
    types = DeviceType.objects.all()
    devices = Device.objects.all()
    contract_devices = instance.devices.all()
    selected_devices_table = tables.SelectedDeviceBottomTable(contract_devices)
    non_contract_devices = [device for device in devices if device not in contract_devices]
    non_contract_table = tables.DeviceModalTable(non_contract_devices)
    return {
      'sites': sites,
      'roles': roles,
      'types': types,
      'selected_devices_table': selected_devices_table,
      'non_contract_table': non_contract_table,
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

@require_http_methods(["POST"])
def add_device_to_contract(request, contract_id):
  try:
    data = json.loads(request.body)
    device_id = data.get("device_id")
    contract = get_object_or_404(models.Contract, pk=contract_id)
    device = get_object_or_404(Device, pk=device_id)
    contract.devices.add(device)
    return JsonResponse({"success":True, "message": "Device added successfully"})
  except Exception as e:
    return JsonResponse({"success":False, "error": str(e), "status": 400})
  
@require_http_methods(["POST"])
def remove_device_from_contract(request, contract_id):
  try:
    data = json.loads(request.body)
    device_id = data.get("device_id")
    contract = get_object_or_404(models.Contract, pk=contract_id)
    device = get_object_or_404(Device, pk=device_id)
    contract.devices.remove(device)
    return JsonResponse({"success":True, "message": "Device remove successfully"})
  except Exception as e:
    return JsonResponse({"success":False, "error": str(e), "status": 400})