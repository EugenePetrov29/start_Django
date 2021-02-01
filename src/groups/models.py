from django.db import models

# Create your models here.
class Groups(models.Model):
    group_name = models.CharField('Group', max_length = 30)

    def __str__(self):
        return self.group_name

class Users(models.Model):
    user_name = models.CharField('User status', max_length = 80)
    user_group = models.ForeignKey(
        Groups,
        on_delete=models.CASCADE,
        related_name="Users",
        null = True,
        blank = True)

    def __str__(self):
        return self.user_name