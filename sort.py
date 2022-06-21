import codecs

# I used this to process a textfile which had a few 
# punctuation marks, "and" & "s" that were repeated at 
# the begining of some sentences.
# you can tweak it to fit your needs


# add other unwanted punctuation marks and symbols here
pnc = [".", ",", "?", "-", ",|", "s", "and"] 
newlines = []
f = codecs.open('generated_text.txt', 'r', "utf-8")
lines = f.readlines()
raw_shitpost = [lin for lin in lines]
print("cleaning...")
for dirtyline in raw_shitpost:
    
    # break up the line into all words and characters in it separated by a space
    splittedline = dirtyline.split(" ")
    listed = [word for word in splittedline]
    
    # index for the first word in the list
    ist = listed[0]
    
    # loop through the unwanted characters list and deletes them if it's found in index 0
    for p in pnc:
        if ist == p:
            listed.remove(ist)
            
    # replace comas at the end of every sentence with a fullstop
    if "," == ist[-1]:
        ist[-1] = "."
        
    # putting the characters back together
    cleanline = " ".join(listed)
    
    # added a new line so no line breaks are added if the line is too long (i used this as a workaround)
    newlines.append(cleanline+"\n")
print("done cleaning")
print("deleting short lines...")


# delete short lines (they mostly dont make any sense if you generated them with a bad model)
qualifiedlines = [line for line in newlines if len(line) > 19]

f = codecs.open('final_product.txt', 'w', 'utf-8')
for lne in qualifiedlines:
    f.write(lne)

print("done")
