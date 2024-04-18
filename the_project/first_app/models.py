from django.db import models

# Create your models here.

class Members(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 100)

    # prevents the entire object from being revealed when a hacker tries to print the object
    def __str__(self):
        return self.name
    

class Address(models.Model):
    id = models.AutoField(primary_key=True)
    street_name = models.CharField(max_length=500)
    level = models.SmallIntegerField()
    unit = models.SmallIntegerField()
    member = models.ForeignKey(Members, on_delete=models.DO_NOTHING, null=True)
    # member = models.ManyToManyField(Members)
    # member = models.OneToOneField(Members, on_delete=models.DO_NOTHING, null=True)
    
    def __str__(self):
        return self.street_name