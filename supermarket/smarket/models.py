from django.db import models

class SmarketUsers(models.Model):
    username = models.TextField()
    password = models.TextField(default='defautpasswordfortesting')
    email = models.TextField(blank=True)
    
    class Meta:
            db_table = 'smarket_users'
# Create your models here.
