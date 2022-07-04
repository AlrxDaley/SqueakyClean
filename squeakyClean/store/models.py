from django.db import models

# Create your models 
class Special(models.Model):
        
        special_id_1 = models.CharField(max_length=254, null=True, blank=True)
        special_id_2 = models.CharField(max_length=254, null=True, blank=True)
        special_id_3 = models.CharField(max_length=254, null=True, blank=True)
        # special_name = models.CharField(max_length=254, null=True, blank=True)
        # special_id = models.IntegerField()
        
        # def __str__(self):
        #     return self.special_name