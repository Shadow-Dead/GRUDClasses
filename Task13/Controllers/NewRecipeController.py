from Task13.Models.RecipeModel import *

class RecipeController:
    @classmethod
    def add(cls,name,cooking_time,difficulty,**kwargs):
        Recipe.create(name=name,ingredients=list(**kwargs),cooking_time=cooking_time,difficulty=difficulty)
    @classmethod
    def get(cls):
        return Recipe.select()