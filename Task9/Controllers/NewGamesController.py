from Task9.Models.GamesModel import *

class GamesController:
    @classmethod
    def add(cls,title,genre,platform,completed=False):
        GamesModel.create(title=title,genre=genre,platform=platform,completed=completed)
    @classmethod
    def get(cls):
        return GamesModel.select()
    @classmethod
    def completed(cls,id):
        GamesModel.update(completed=True).where(GamesModel.id == id).execute()
    @classmethod
    def find_by_genre(cls,genre):
        return GamesModel.select().where(GamesModel.genre == genre)
    @classmethod
    def find_by_platform(cls,platform):
        return GamesModel.select().where(GamesModel.platform == platform)

if __name__ == "__main__":
    # GamesController.add("The Witcher", "RPG", "PC")
    # GamesController.add("Battlefield 6", "FPS", "PC")
    # GamesController.add("God of War", "RPG", "PS4")
    GamesController.completed(3)
    for i in GamesController.get():
        print(i.id,i.title,i.genre,i.platform,i.completed)
    for i in GamesController.find_by_genre("RPG"):
        print(i.id,i.title,i.genre,i.platform,i.completed)
    for i in GamesController.find_by_platform("PC"):
        print(i.id,i.title,i.genre,i.platform,i.completed)