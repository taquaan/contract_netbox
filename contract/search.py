from netbox.search import SearchIndex, register_search
from .models import Contract, Supplier

@register_search
class ContractIndex(SearchIndex):
    model = Contract
    fields = (
        ('name', 100),
        ('comments', 5000),
    )

@register_search
class SupplierIndex(SearchIndex):
    model = Supplier
    fields = (
        ('name', 100),
    )