
def print_movies(movies):
    for i, item in enumerate(movies):
        if(isinstance(item,list)):
            print_movies(item)
        else:
            print("{0}: {1}".format(i,item))
