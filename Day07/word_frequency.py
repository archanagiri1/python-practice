sentence= "python is very easy and python is powerfull"

words= sentence.split()
freq={}

for w in words:
    freq[w]= freq.get(w,0)+1

    print(freq)
