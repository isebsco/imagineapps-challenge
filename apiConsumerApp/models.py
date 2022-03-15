from django.db import models
from django.conf import settings

import collections
import jsonfield

class CocoaContracts(models.Model):
    id   = models.AutoField(primary_key=True)
    data = jsonfield.JSONField(blank=True, null=True, load_kwargs={'object_pairs_hook': collections.OrderedDict})
    
    def __str__(self):
        return self.id