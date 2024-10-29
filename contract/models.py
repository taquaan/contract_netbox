from netbox.models import NetBoxModel
from django.db import models
from django.urls import reverse
from utilities.choices import ChoiceSet

class StatusChoice(ChoiceSet):
  key = 'Contract.status'
  CHOICES = [
      ('active', 'Active', 'green'),
      ('cancel', 'Canceled', 'red'),
  ]

# SUPPLIER 
class Supplier(NetBoxModel):
  name = models.CharField(max_length=100)
  phone = models.CharField(max_length=12)
  email = models.EmailField(max_length=50)
  slug = models.SlugField(max_length=30)
  
  class Meta:
    ordering = ('name',)
    
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('plugins:contract:supplier', args=[self.pk])

# CONTRACT
class Contract(NetBoxModel):
  name = models.CharField(
    max_length=100
  )
  tenant = models.ForeignKey(
    to='tenancy.Tenant',
    on_delete=models.PROTECT,
    related_name='contracts',
    blank=True,
    null=True,
  )
  status = models.CharField(
    max_length=50,
    choices=StatusChoice,
  )
  devices = models.ManyToManyField(
    'dcim.Device',
    related_name="contracts",
    blank=True,
  )
  supplier = models.ForeignKey(
    Supplier,
    on_delete=models.PROTECT,
    related_name='contracts',
    blank=True,
    null=True,
  )
  start_date = models.DateField(blank=True, null=True)
  end_date = models.DateField(blank=True, null=True)
  renewal_term = models.IntegerField(
    help_text='In months', default=12, blank=True, null=True
  )
  comments = models.TextField(blank=True)
  
  def get_absolute_url(self):
    return reverse('plugins:contract:contract', args=[self.pk])
  
  class Meta:
    ordering = ('name',)
  
  def __str__(self):
    return self.name