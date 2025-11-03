class FoodDiary:
    def __init__(self):
        self.__meals = [
            {"id": 1, "meal": "Завтрак", "food": "Овсянка", "calories": 300, "time":"08:00"}
        ]
        self.__id = 2
    @property
    def meals(self):
        return self.__meals
    @meals.setter
    def meals(self,dict):
        dict['id'] = self.__id
        self.__meals.append(dict)
        self.__id += 1

if __name__ == "__main__":
    foods = FoodDiary()
    print(foods.meals)
    foods.meals={"id": 1, "meal": "Завтрак", "food": "Йогурт", "calories": 200, "time":"08:00"}
    print(foods.meals)
