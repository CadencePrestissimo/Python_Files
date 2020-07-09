import imdb
x = imdb.IMDb()
'''Enter the movie'''
print("Enter the movie : ")
a = input()
search=x.search_movie(a)
year= search[0]['year']
print(search[0]['title']+": "+str(year))