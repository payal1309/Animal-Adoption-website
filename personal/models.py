from django.db import models



class InterestedPeople(models.Model):
	email = models.URLField(max_length=255)
	name = models.CharField(max_length=255)
	address = models.TextField(max_length=10000)
	number = models.IntegerField()
	animalname = models.TextField(max_length=10000)
	whatsapp = models.TextField(max_length=255)
	instagram = models.TextField(max_length=255)
	facebook = models.TextField(max_length=255)
 


	def __str__(self):
   	 return self.title + ' ' + self.display

# #Two tuple structure
# #The first element in each tuple is the value that will be stored in the database. The second element is displayed by the field’s form widget.
# #Tuple
# PRIORITY = [
# 	('L', 'Low'), #Tuple1
# 	('M', 'Medium'), #Tuple2
# 	('H', 'High'), #Tuple3
# ]

# class Question(models.Model):
# 	title		 			= models.CharField(max_length=60)
# 	question 				= models.TextField(max_length=400)
# 	priority 				= models.CharField(max_length=1, choices=PRIORITY)

# 	def __str__(self):
# 		return self.title


# 	class Meta:
# 		verbose_name = 'The Question'
# 		verbose_name_plural = 'Questions from People'