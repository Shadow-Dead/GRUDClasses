from Task13.Models.Recipe import Recipe

class RecipeController:
    obj = Recipe()
    @classmethod
    def get(cls):
        return cls.obj.recipes
    @classmethod
    def add(cls,name,cooking_time,difficulty, *ingredients):
        # new_ingredients = []
        # for i in ingredients:
        #     new_ingredients.append(i)
        # new_new_ingredients = [i for i in ingredients]

        dict = {
            "name": name,
            # "ingredients": [i for i in ingredients],
            "ingredients": list(ingredients),
            "cooking_time": cooking_time,
            "difficulty": difficulty,
        }
        cls.obj.recipes = dict
        return dict

if __name__ == "__main__":
    print(RecipeController.get())
    print(RecipeController.add(
        "Яичница",
        7,
        "легкая",
        "яйцо",
        "лук",
        "масло"
    ))
    print(RecipeController.get())
