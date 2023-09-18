from django.db import models


# Create your models here.
class Company(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    obym_upakov = models.IntegerField(null=True)
    vid_upakov = models.CharField(max_length=20)
    recomen = models.BooleanField()
    firma = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    # if __name__ == '__main__':
    #     bot.polling(none_stop=True, interval=0)


class Course(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Student(models.Model):
    name = models.CharField(max_length=10)
    grop = models.CharField(max_length=4)
    course = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)