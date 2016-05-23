from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=200, unique=True)
    name_jp = models.CharField(max_length=200, blank=True)
    age = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=7)
    first_appearance = models.IntegerField()
    desc = models.TextField(blank=True)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Place(models.Model):
    name = models.CharField(max_length=200, unique=True)
    location = models.CharField(max_length=200, blank=True)
    first_appearance = models.IntegerField()
    desc = models.TextField(blank=True)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=200, unique=True)
    name_jp = models.CharField(max_length=200, blank=True)
    org_type = models.CharField(max_length=200)
    active = models.CharField(max_length=7)
    leader = models.ForeignKey(Character, blank=True, null=True)
    base = models.ForeignKey('Place', blank=True, null=True)
    first_appearance = models.IntegerField()
    desc = models.TextField(blank=True)
    
    def publish(self):
        self.save()

    def __str__(self):
        return self.name


class Membership(models.Model):
    key = models.IntegerField(unique=True);
    character_name = models.ForeignKey('Character')
    org_name = models.ForeignKey('Organization')
    
    def publish(self):
        self.save()

    def __str__(self):
        return str(self.key)

