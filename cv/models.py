from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name on resume")
    email = models.EmailField(verbose_name="Email address of person")
    github_id = models.CharField(max_length=30, verbose_name="GitHub ID of person")
    goal = models.TextField(verbose_name="Purpose/goal of the person")

    def __str__(self):
        return "CV for %s" % self.name


class Publication(models.Model):
    authors = models.CharField(max_length=500, verbose_name="Pre-prettified list of authors")
    year = models.IntegerField(verbose_name="Year of publication")
    title = models.CharField(max_length=500, verbose_name="Title of publication")
    container = models.CharField(max_length=500, verbose_name="Pre-prettified conference or journal information")

    def __str__(self):
        return "%s: %s" % (self.year, self.authors)


class Education(models.Model):
    degree = models.CharField(max_length=100, verbose_name="Education degree, such as Doctor of Philosophy")
    field = models.CharField(max_length=100, verbose_name="Name of the field, such as Mechanical Engineering")
    date = models.CharField(max_length=100, verbose_name="Date of degree, shortened, such as May 2013")
    school = models.CharField(max_length=100, verbose_name="The name of the university")
    thesis = models.CharField(max_length=100, verbose_name="Title of thesis if a thesis was completed")
    gpa = models.FloatField(verbose_name="The numeric GPA for this degree")

    def __str__(self):
        return "%s: %s" % (self.degree, self.field)


class Experience(models.Model):
    title = models.CharField(max_length=100, verbose_name="Job title")
    date = models.CharField(max_length=100, verbose_name="Descriptive time frame working for this company")
    company = models.CharField(max_length=100, verbose_name="Company name")
    json_description = models.TextField(verbose_name="A JSON string description of job responsibilities, etc.", null=True)
    json_blob = None


class Skill(models.Model):
    description = models.TextField(verbose_name="A description of this skill")


class MembershipItem(models.Model):
    description = models.TextField(verbose_name="An attribute of this membership")


class ProjectAttribute(models.Model):
    description = models.TextField(verbose_name="An attribute of this project")
