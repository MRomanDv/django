from django.db import models

# Create your models here. this model will be the structure of our SQL database
#enherance properties of Model
class Book(models.Model):
    title = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    publish_date = models.DateField()
    quantity = models.IntegerField()
#def __str__ represtents the str representation of the object in this case that would be the title
    def __str__(self):
        return self.title


#Books/list        