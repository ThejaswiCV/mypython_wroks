from json import load

path="C:\\Users\\Sinju\\Desktop\\mypython\\movies\\db.json"

with open(path) as f:
    data=load(f)
    
# print(len(data))

all_names=[m.get("Title") for m in data]    
# print(all_names)

all_directors={m.get("Director") for m in data}
all_directors.discard("N/A")
# print(all_directors)

all_rating=[m.get("imdbRating") for m in data]
# print(all_rating)

#high rating
filter_NA=[m for m in data if m.get("imdbRating")!="N/A"]

high_rating=max(filter_NA,key=lambda m:float( m.get("imdbRating")))
# print(high_rating.get("Title"))


#take all genre
all_genres=set()
for m in data:
    for gn in m.get("Genre").split():
        all_genres.add(gn.rstrip(","))        
# print(all_genres)   


#take movies with action genre
# for mv in data:
#     if mv.get("Genre").count("Action")>0:
#         print(mv.get("Title"))
        
        
#all movies released after 2014
for mov in data:
    r_date=mov.get("Released")
    year=r_date.split(" ")[-1]
    if year.isdigit():
        if int(year)>2014:
            print(mov.get("Title"))     


        
        
        
        

    



       
        




















