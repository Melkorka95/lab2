from django.db import models


class Character(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    UNKNOWN = 'U'
    NONE = 'N'
    ALIVE = 'L'
    DECEASED = 'D'
    SPIRIT = 'S'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (UNKNOWN, 'Unknown'),
        (NONE, 'Genderless')
    )
    STATUS_CHOICES = (
        (ALIVE, 'Alive'),
        (DECEASED, 'Deceased'),
        (SPIRIT, 'Cait Sith'),
        (UNKNOWN, 'Unknown')
    )
    name = models.CharField(max_length=200, unique=True)
    name_jp = models.CharField(max_length=200, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=UNKNOWN)
    age = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=ALIVE)
    first_appearance = models.IntegerField()
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200, blank=True)
    first_appearance = models.IntegerField()
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    ACTIVE = 'A'
    INACTIVE = 'I'
    UNKNOWN = 'U'
    ST_CHOICES = (
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
        (UNKNOWN, 'Unknown')
    )
    name = models.CharField(max_length=200, unique=True)
    name_jp = models.CharField(max_length=200, blank=True)
    org_type = models.CharField(max_length=200, blank=True)
    active = models.CharField(max_length=8, choices=ST_CHOICES, default=ACTIVE)
    base = models.ForeignKey('Place', blank=True, null=True)
    leader = models.ForeignKey('Character', blank=True, null=True)
    first_appearance = models.IntegerField()
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Membership(models.Model):
    key = models.IntegerField(unique=True);
    character_name = models.ForeignKey('Character')
    org_name = models.ForeignKey('Organization')

    def __str__(self):
        return str(self.key)

