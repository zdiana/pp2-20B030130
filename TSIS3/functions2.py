
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]#1
def check_score_greater(movie): 
    if(movie['imdb']>5.5):
       return True
    else:
        return False
#for movie in movies:
 #   if check_score_greater(movie):
  #      print ("True")
   # else:
    #    print ("False")


#2
def check_imdb_score(movie):
    return movie["imdb"] > 5.5


#for movie in movies:
   # if check_imdb_score(movie):
        #print("{} has an IMDB score above 5.5".format(movie["name"]))


#3
def check_category(movies, category):
    list_of_ct_films = []
    for movie in movies:
        current_cat_film = movie['category']
        if category == current_cat_film:
            list_of_ct_films.append(movie)
    return list_of_ct_films

#list_of_ct_films = check_category(movies, 'Romance')
#print(list_of_ct_films)



#4

def average_imdb(movies): 
    avg_score=0
    total_movies=len(movies)
    for movie in movies:
        avg_score=avg_score+movie['imdb']
    avg_score=avg_score/total_movies
    return avg_score
    
#x=average_imdb(movies)
#print (x)


#5

def avg_imdb_cat(movies,category_names):
    cat_movies=check_category(movies,category_names)
    avg_score=average_imdb(cat_movies)
    return avg_score
   
y=avg_imdb_cat(movies,'Thriller')
print (y)
  