from netbox.plugins import PluginConfig

class ContractConfig(PluginConfig):
    name = 'contract'
    verbose_name = 'Contract'
    description = 'An NetBox plugin for Contract Management'
    version = '0.1'
    author = 'taquan'
    author_email = 'taquan@gmail.com'
    base_url = 'contract'
    required_settings = []

config = ContractConfig