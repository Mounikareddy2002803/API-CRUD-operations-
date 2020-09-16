from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name=models.CharField(max_length=50,primary_key=True)

    def __str__(self):
        return self.topic_name


class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,unique=True)
    url=models.URLField()

    def __str__(self):
        return self.name

class Access_Records(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField(auto_now=True)




#auto_now=True
'''

if date is given then i will consider the given date

if u r not providing
then 
models r created on 5-sep-2020

inserting the data on 5-sep-2020

date=5-sep-2020

inserting the data on 10-sep-2020

date=10-sep-2020





auto_now_add=True

if date is given then i will consider the given date

if u r not providing then 

models r created on 5-sep-2020

inserting the data on 5-sep-2020

date=5-sep-2020

inserting the data on 10-sep-2020

date=5-sep-2020

'''








