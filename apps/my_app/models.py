from django.db import models

class Poll(models.Model):
	label = models.CharField(verbose_name='label', max_length=100)
	priority = models.CharField('priority level', max_length=10)
	number = models.PositiveIntegerField()

	def __str__(self):
		return self.label

class Reply(models.Model):
	label = models.CharField(verbose_name='label', max_length=100)
	# here we define that a reply is always relate to a poll object
	# a poll object is bound to 0 or N reply objects
	poll = models.ForeignKey(Poll)
	
	def __str__(self):
		return self.label