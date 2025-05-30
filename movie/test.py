class Movie:
    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        print("movie Name:", self.title)
        print("Hero Name", self.hero)
        print("Heroine Name", self.heroine)

list_of_movies =[]
while True:
    title=input("Enter the movie name:")
    hero=input("Enter the Hero Name:")
    heroine=input("Enter the Heroine Name:")
    m=Movie(title,hero,heroine)
    list_of_movies.append(m)
    print("Movie added to the list successfully")
    option=input("Do you want to add one more movie [Yes|No]:")
    if option.lower() == "no":
        break
print("All Movies Information")
print("#"*100)
for movie in list_of_movies:
    movie.info()
    print()

