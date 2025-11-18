from Task17.Models.MusicModel import *

class MusicController:
    @classmethod
    def add(cls,title,artist,album,year,genre):
        MusicModel.create(title=title,artist=artist,album=album,year=year,genre=genre)
    @classmethod
    def get(cls):
        return MusicModel.select()
    @classmethod
    def find_by_artist(cls,artist):
        return MusicModel.select().where(MusicModel.artist == artist)
    @classmethod
    def find_by_genre(cls,genre):
        return MusicModel.select().where(MusicModel.genre == genre)
    @classmethod
    def album_year(cls,year):
        return MusicModel.select().where(MusicModel.year == year)

if __name__ == "__main__":
    # MusicController.add("Bohemian Rhapsody","Queen","A Night at the Opera",1975,"рок")
    # MusicController.add("Вечно молодой","Смысловые галлюцинации","3000",2000,"рок")
    for i in MusicController.get():
        print(i.id,i.title,i.artist,i.album,i.year,i.genre)
    for i in MusicController.find_by_artist("Queen"):
        print(i.id,i.title,i.artist,i.album,i.year,i.genre)
    for i in MusicController.find_by_genre("рок"):
        print(i.id,i.title,i.artist,i.album,i.year,i.genre)
    for i in MusicController.album_year(1975):
        print(i.id,i.title,i.artist,i.album,i.year,i.genre)