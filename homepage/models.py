from django.db import models

# Create your models here.
class Developer(models.Model):
	name=models.CharField(max_length=200,null=True)
	job=models.TextField(null=True)

	def __str__(self):
		return self.name
class My_work(models.Model):
	name=models.CharField(max_length=200,null=True)
	description=models.TextField(null=True)
	lang1=models.CharField(max_length=200,null=True)
	lang2=models.CharField(max_length=200,null=True)
	lang3=models.CharField(max_length=200,null=True)
	lang4=models.CharField(max_length=200,null=True)
	lang5=models.CharField(max_length=200,null=True)
	lang6=models.CharField(max_length=200,null=True)
	link_github=models.TextField(null=True)
	link_site=models.TextField(null=True)
	img1=models.ImageField(upload_to="media/img")
	img2=models.ImageField(upload_to="media/img")
	def __str__(self):
		return self.name

class About(models.Model):
	description = models.TextField(null=True)
	description2=models.TextField(null=True)
	img1 = models.ImageField(upload_to="media/img")

	mail=models.TextField(null=True)
	telegram=models.TextField(null=True)
	phone=models.TextField(null=True)
	github=models.TextField(null=True)


	def __str__(self):
		return "about"





class File(models.Model):
	resume = models.FileField(upload_to="media/resume")
	title=models.CharField(max_length=50)

	def __str__(self):
		return "resume"









