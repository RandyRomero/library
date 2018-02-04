from django.db import models


class Author(models.Model):
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    patronym = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    phone_number = models.CharField(max_length=75, blank=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name


class Tag(models.Model):
    name = models.CharField('Tag name', max_length=50)
    flag = models.BooleanField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField('Book Title', max_length=200)
    pub_date = models.DateField('date published')
    description = models.CharField(max_length=1000)
    thumbnail = models.ImageField(upload_to='thumbnails', blank=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
