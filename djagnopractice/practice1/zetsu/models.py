from django.db import models
from django.contrib.auth.base_user import BaseUserManager,AbstractBaseUser
# Create your models here.
class Anime(BaseUserManager):

    def create_user(self, firstname, lastname, email, username, fav_character, password=None, **extra_fields):
        if not email:
            raise ValueError("Can't remember mailID properly? what a waste...")
        if not username:
            raise ValueError("Did you forgot how your called? pathetic!")
        if not fav_character:
            raise ValueError("Ignorant is bliss not forgetting you moron! ")

        user = self.model(username=username, email=self.normalize_email(email), firstname=firstname, lastname=lastname,
                          fav_character=fav_character)

        user.set_password(password)
        user.save()
        return user


class Donguha(AbstractBaseUser):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField(max_length=50,unique=True)
    fav_character = models.CharField(max_length=25)

    objects=Anime()
