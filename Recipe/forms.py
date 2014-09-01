from django.forms.models import inlineformset_factory, ModelForm
from Recipe.models import Recipe, Ingredient, RecipeStep

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe

# Ingredients and recipe steps should be added via an inline form on the parent recipe form
# We exclude the recipe field as we set this when save the form
IngredientFormSet = inlineformset_factory(Recipe, Ingredient, exclude=('recipe',))
RecipeStepFormSet = inlineformset_factory(Recipe, RecipeStep, exclude=('recipe',))
