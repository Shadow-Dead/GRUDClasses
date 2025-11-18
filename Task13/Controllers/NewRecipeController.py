from Task13.Models.RecipeModel import *

class RecipeController:
    @classmethod
    def add(cls,name,cooking_time,difficulty,*ingredients):
        Recipe.create(name=name,ingredients=list(ingredients),cooking_time=cooking_time,difficulty=difficulty)
    @classmethod
    def get(cls):
        return Recipe.select()
    @classmethod
    def find_by_ingredient(cls,ingredient):
        return Recipe.select().where(Recipe.ingredients.contains(ingredient))
    @classmethod
    def fast_recipe(cls):
        return Recipe.select().where(Recipe.cooking_time <= 30)

if __name__ == "__main__":
    # RecipeController.add("Борщ",120,"средняя","свекла", "капуста", "мясо")
    # RecipeController.add("Омлет",20,"легкая","яйца", "молоко")
    for i in RecipeController.get():
        print(i.id,i.name,i.cooking_time,i.difficulty,i.ingredients)
    for i in RecipeController.find_by_ingredient("мясо"):
        print(i.id,i.name,i.cooking_time,i.difficulty,i.ingredients)
    for i in RecipeController.fast_recipe():
        print(i.id,i.name,i.cooking_time,i.difficulty,i.ingredients)