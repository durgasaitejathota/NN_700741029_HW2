#define a empty string
st = ""

#define a function to count occurances of each word
def wordcount(st):
    counts = dict()
    w = st.split()
    for y in w:
        if y in counts:
            counts[y]+=1
        else:
            counts[y]=1
    return counts
#read input.txt file and adding it to st variable
with open(r'input.txt','r') as file:
    data = file.read()
    st +=data

#call wordcount function
a=str(wordcount(st))
st+="\nWord_Count: \n"
st+=a

#replace string to get required output
st = st.replace("{","")
st = st.replace("}","")
st = st.replace("'","")
st = st.replace("P","\nP")
st = st.replace(", ","\n")
print(st)


outputfile = open(r'output.txt','w')
outputfile.write(st)

#closing of txt files
outputfile.close()
file.close()
