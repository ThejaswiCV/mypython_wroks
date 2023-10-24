text="i have one car 2 bikes and 3 cycles"
# >>print the numbers only

words=text.split(" ") #split the text [i ,have ,one ,car ,2, bikes, and ,3, cycles]

for w in words:   #i #have #...etc 
    if w.isdigit(): #check with each words whether it is digit or not
        print(w)  