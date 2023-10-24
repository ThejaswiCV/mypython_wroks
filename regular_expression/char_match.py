from re import*
#               9101112
text="abcdABCDE @K&9"
#     012345678
# pattern="[a-d]"         #match either a b c or d             #or "[abcd]"

#pattern="[0-9]"             #digit only

# pattern="[a-zA-Z0-9]"

# pattern="[^a-z]"                  #exclude lower case a to z characters

# pattern="[^A-Za-z]"               #exclude all alphabet

# pattern="[^a-zA-Z0-9]"            #exclude alphanumeric values and digit . so only spl character

# pattern="\d"                      # "[0-9]" ie digit only .here predefined character

# pattern="\D"                      # "[^0-9]" ie exclude digit

# pattern="\w"                      # "[a-zA-Z0-9]" .alpha numeric digit only. no spl ch

pattern="\W"                        # "[^a-zA-Z0-9]" . exclude alpha numeric digit. only spl ch

matcher=finditer(pattern,text)      #[s=0,g=a  s=1,g=b  s=2,g=c  s=3,g=d]               

for m in matcher:
    print(m.start(),m.group())            
    
    