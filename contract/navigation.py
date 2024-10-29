from netbox.plugins import PluginMenuItem, PluginMenuButton
from netbox.choices import ButtonColorChoices

menu_items = ()

contract_buttons = [
    PluginMenuButton(
        link='plugins:contract:contract_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.WHITE
    )
]

supplier_buttons = [
    PluginMenuButton(
        link='plugins:contract:supplier_add',
        title='Add',
        icon_class='mdi mdi-plus-thick',
        color=ButtonColorChoices.WHITE
    )
]

menu_items = (
    PluginMenuItem(
        link='plugins:contract:contract_list',
        link_text='Contracts',
        buttons=contract_buttons,
    ),
    PluginMenuItem(
        link='plugins:contract:supplier_list',
        link_text='Suppliers',
        buttons=supplier_buttons,
    ),
)