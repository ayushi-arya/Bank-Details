from django.db import models

 from django.db import models

 class Bank(models.Model):
     name = models.CharField(max_length=50)

     class Meta:
         ordering = ('name',)

     def __str__(self):
         return "{}".format(self.name)

 class Branch(models.Model):
     name = models.CharField(max_length=256)  # branch 
     ifsc = models.CharField(max_length=20, unique=True)
     bank = models.ForeignKey(Bank)
     address = models.TextField()
     city = models.CharField(max_length=20)
     district = models.CharField(max_length=50)
     state = models.CharField(max_length=20)

     class Meta:
         ordering = ('name',)
         verbose_name = 'Branch'
         verbose_name_plural = 'Branch'

     def __str__(self):
         return "{} - {} - {}".format(self.name, self.city, self.bank) 
