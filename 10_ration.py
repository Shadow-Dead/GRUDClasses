class FoodDiary:
    def __init__(self):
        self.__meals = [
            {"id": 1, "meal": "Завтрак", "food": "Овсянка", "calories": 300, "time":"08:00"}
        ]
        self.__id = 2
    @property
    def meals(self):
        return self.__meals

    def add(self, meal, food, calories, time):
        self.__meals.append(
            {
                "id": self.__id,
                "meal": meal,
                "food": food,
                "calories": calories,
                "time": time
            }
        )
        self.__id += 1
        return True

    def calories(self):
        summa=0
        for i in self.__meals:
            summa+=i["calories"]
        return summa

    def find_by_time(self,time):
        lst=[]
        for i in self.__meals:
            if i['time'] == time:
                lst.append(i)
        return lst

if __name__ == "__main__":
    foods = FoodDiary()
    print(foods.add('Завтрак',"Йогурт",200,"08:00"))
    print(foods.add('Обед',"Куринный суп",400,"12:00"))
    print(foods.meals)
    print(foods.calories())
    print(foods.find_by_time("08:00"))