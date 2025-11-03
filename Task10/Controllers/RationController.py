from Task10.Models.Ration import FoodDiary

class RationController:
    obj = FoodDiary()
    @classmethod
    def add(cls, meal, food, calories, time):
        cls.obj.meals={
                "id": 0,
                "meal": meal,
                "food": food,
                "calories": calories,
                "time": time
        }
        return True

    @classmethod
    def get(cls):
        return cls.obj.meals
    
    @classmethod
    def calories(cls):
        summa=0
        for i in cls.get():
            summa+=i["calories"]
        return summa

    @classmethod
    def find_by_time(cls,time):
        lst=[]
        for i in cls.get():
            if i['time'] == time:
                lst.append(i)
        return lst

if __name__ == "__main__":
    print(RationController.add('Завтрак',"Йогурт",200,"08:00"))
    print(RationController.add('Обед',"Куринный суп",400,"12:00"))
    print(RationController.get())
    print(RationController.calories())
    print(RationController.find_by_time("08:00"))