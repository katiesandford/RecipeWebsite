from django.contrib import admin
from Recipe.models import Recipe, Ingredient, RecipeStep

class IngredientsAdmin(admin.TabularInline):
    model = Ingredient
    
class RecipeStepAdmin(admin.TabularInline):
    model = RecipeStep

class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientsAdmin,
        RecipeStepAdmin
    ]

admin.site.register(Recipe, RecipeAdmin)
