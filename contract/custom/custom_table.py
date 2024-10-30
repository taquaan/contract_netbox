from netbox.tables.columns import ActionsColumn
from netbox.tables.tables import NetBoxTable
from dcim.models import Device

class CustomActionsColumn(ActionsColumn):
  def __init__(self, *args, **kwargs):
    extra_buttons = '''
    <a class="btn btn-sm btn-success" href="#" contract_id=record.pk %}" aria-label="Add">
        <i class="mdi mdi-plus"></i> Add
    </a>
    '''
    super().__init__(*args, extra_buttons=extra_buttons, **kwargs)
    
class CustomNetBoxTable(NetBoxTable):
    actions = CustomActionsColumn()
    
    class Meta(NetBoxTable.Meta):
      model = Device
      fields = ('pk', 'id', 'name', 'status', 'tenant', 'site','location', 'rack', 'role', 'manufacturer', 'device_type')
      default_columns = ('name', 'status', 'tenant', 'site','location', 'rack', 'role', 'manufacturer', 'device_type')