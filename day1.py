
def print_movies(movies):
    for i, item in enumerate(movies):
        if(isinstance(item,list)):
            print_movies(item)
        else:
            print("{0}: {1}".format(i,item))

def main():
    movies = ["Dark night Rises",2008, "Christopher Nolan","The Terminal",
               2004, "Stephen Spielberg", "Inception", 2010, "Christopher Nolan"]
    movies.insert(6, "Momento")
    movies.append("The Darknight Rises")
    movies.pop()
    movies.pop(1)
    movies.remove("The Terminal")
    cast = ["aaaa","bbbb","cccc"]
    movies.append(cast)
    print_movies(movies)

if __name__ == "__main__":
    main()
