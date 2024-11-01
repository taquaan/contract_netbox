from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
from .models import Contract, Supplier
from utilities.forms.fields import CommentField, DynamicModelChoiceField, DynamicModelMultipleChoiceField, SlugField
from utilities.forms.widgets import DatePicker
from tenancy.models import Tenant
from dcim.models import Device
from tenancy.models import Tenant

class ContractForm(NetBoxModelForm):
  comments = CommentField()
  tenant = DynamicModelChoiceField(queryset=Tenant.objects.all(), required=False)
  devices = DynamicModelMultipleChoiceField(queryset=Device.objects.all(), required=False)
  
  class Meta:
    model = Contract
    fields = ('name', 'tenant', 'status', 'devices', 'tenant', 'supplier', 'start_date', 'end_date')
    widgets = {
      'start_date': DatePicker(),
      'end_date': DatePicker(),
    }
    
class SupplierForm(NetBoxModelForm):
  slug = SlugField()
  
  class Meta:
    model = Supplier
    fields = ('name', 'phone', 'email')
    
class SupplierFilterForm(NetBoxModelFilterSetForm):
  model = Supplier
  name = forms.CharField(max_length=100, required=False)
  phone = forms.CharField(max_length=30, required=False)
  email = forms.CharField(max_length=50, required=False)
  
class ContractFilterForm(NetBoxModelFilterSetForm):
  model = Contract
  name = forms.CharField(max_length=100, required=False)
  tenant = forms.ModelMultipleChoiceField(
    queryset=Tenant.objects.all(),
    required=False
  )
  supplier = forms.ModelMultipleChoiceField(
    queryset=Supplier.objects.all(),
    required=False
  )