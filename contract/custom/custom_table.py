from netbox.tables.columns import ActionsColumn
from netbox.tables.tables import NetBoxTable
from dcim.models import Device

class CustomActionsColumn(ActionsColumn):
  def __init__(self, *args, **kwargs):
    extra_buttons = '''
    <a class="add-device-contract btn btn-sm btn-success" device_id={{record.pk}} %}" aria-label="Add">
        <i class="mdi mdi-plus"></i> Add
    </a>
    '''
    super().__init__(*args, extra_buttons=extra_buttons, **kwargs)
    
class CustomRemoveActionsColumn(ActionsColumn):
    def __init__(self, *args, **kwargs):
      extra_buttons = '''
      <a class="remove-device-contract btn btn-sm btn-danger" device_id={{record.pk}} %}" aria-label="Add">
          <i class="mdi mdi-close"></i>
      </a>
      '''
      super().__init__(*args, extra_buttons=extra_buttons, **kwargs)
    
class CustomNetBoxTable(NetBoxTable):
    actions = CustomActionsColumn()
    
    class Meta(NetBoxTable.Meta):
      model = Device
      fields = ('pk', 'id', 'name', 'status', 'tenant', 'site','location', 'rack', 'role', 'manufacturer', 'device_type')
      default_columns = ('name', 'status', 'tenant', 'site','location', 'rack', 'role', 'manufacturer', 'device_type')
      
class CustomRemoveNetBoxTable(NetBoxTable):
    actions = CustomRemoveActionsColumn()
    
    class Meta(NetBoxTable.Meta):
      model = Device
      fields = ('pk', 'id', 'name', 'status', 'tenant', 'site','location', 'rack', 'role', 'manufacturer', 'device_type')
      default_columns = ('name', 'status', 'tenant', 'site','location', 'rack', 'role', 'manufacturer', 'device_type')
