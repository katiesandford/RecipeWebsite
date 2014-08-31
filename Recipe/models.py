from django.db import models
from django.utils.text import slugify

class Recipe(models.Model):
    title = models.CharField("Title", max_length=250)
    created_datetime = models.DateTimeField(auto_now_add=True)
    description = models.TextField("Description")
    
    class Meta:
        ordering = ['-created_datetime']
        
    def __unicode__(self):
        return u'%s' % self.title
    
    def get_absolute_url(self):
        return "/recipe/%i/%s" % (self.id, slugify(self.title))
    
class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='ingredients')
    name = models.CharField("Ingredient", max_length=250)
    quantity = models.FloatField("Quantity")
    units = models.CharField("Units", max_length=50, null=True, blank=True) 
    
    class Meta:
        ordering = ['name']
    
class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='steps')
    rank = models.PositiveIntegerField()
    description = models.TextField("Description")
    
    class Meta:
        ordering = ['rank']
        unique_together= ('rank', 'recipe')
    