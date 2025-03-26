import Book_Exercise as BE
'''
Can represent manhua/manwha.
'''
class Manga(BE.Book):
    def __init__(self, t = None, a = None,
                g = None, p = None, pl = None, c = None, o = None):
        super().__init__(t, a, g, p, pl)
        self.is_colour = c
        self.origin_country = o

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nOrigin: {self.origin_country}"

    def has_anime(self, number_sold):
        return number_sold >= 1000000

if __name__ == "__main__":
    a_manga = Manga("Uzumaki", "Junji Ito", "Horror", "Dark Horse",
                    300, False, "Japan")
    
    print(a_manga)
    print(a_manga.has_anime(10000))
