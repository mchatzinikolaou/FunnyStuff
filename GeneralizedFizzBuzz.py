cor={3:"Fizz",
     5:"Buzz",
     #... add more divisor->String mappings here
}

N=100
for i in range(1,N):
    output=""
    for key in cor.keys():
        if i%key ==0:
            output+=cor[key]
    print (i if output=="" else output)
