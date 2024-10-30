import django_tables2 as tables
from netbox.tables import NetBoxTable

from contract.models import Contract, Supplier
from dcim.models import Device
from contract.custom.custom_table import CustomActionsColumn, CustomNetBoxTable

class ContractListTable(NetBoxTable):
  name = tables.Column(
    linkify=True
  )
  tenant = tables.Column(
    linkify=True
  )
  
  class Meta(NetBoxTable.Meta):
    model = Contract
    fields = ('pk', 'id', 'name', 'tenant', 'status', 'start_date', 'end_date', 'actions')
    default_columns = ('name', 'tenant', 'status', 'start_date', 'end_date')
    
class SupplierListTable(NetBoxTable):
  name = tables.Column(
    linkify=True
  )
  class Meta(NetBoxTable.Meta):
    model = Supplier
    fields = ('pk', 'id', 'name', 'phone', 'email', 'actions')
    default_columns = ('name', 'phone', 'email')
    
class ContractListSideTable(NetBoxTable):
  name = tables.Column(
    linkify=True
  )
  tenant = tables.Column(
    linkify=True
  )
  
  class Meta(NetBoxTable.Meta):
    model = Device
    fields = ('pk', 'id', 'name', 'status', 'start_date', 'end_date','remove')
    default_columns = ('name', 'status', 'start_date', 'end_date')
    
class DeviceModalTable(CustomNetBoxTable):
  name = tables.Column(
    linkify=True
  )
  site = tables.Column(
    linkify=True
  )
  manufacturer = tables.Column(
    linkify=True
  )
  device_type = tables.Column(
    linkify=True
  )
  class Meta(CustomNetBoxTable.Meta):
    model = Device
    