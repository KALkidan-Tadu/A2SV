def converter(Tsize):
    if Tsize =='S' or Tsize =='s':
        return 0
    elif Tsize == 'M' or Tsize == 'm':
        return 1
    else:
        return 2


testCases = int(input())

for i in range(testCases):
    tshirts = input().split()
    tshirt1 = tshirts[0]
    tshirt2 = tshirts[1]
    length1 = len(tshirt1)
    length2 = len(tshirt2)
    size1 = converter(tshirt1[length1-1])
    size2 = converter(tshirt2[length2-1])
    
    x1 = 0
    x2 = 0
    
    for i in range(length1-1):
        x1 += 1
    
    for j in range(length2-1):
        x2 += 1
        
    if size1 > size2 :
        print('>')
    elif size1 < size2 :
        print('<')
    elif size2 == size1:
        if x1 == x2:
            print('=')
        elif size1==0:
            if x1 > x2:
                print('<')
            else:
                print('>')
        else:
            if x1 > x2:
                print('>')
            else:
                print('<')
