if __name__ == '__main__':
    l=[]
    N = int(input())
    for i in range(N):
        command=list(input().split())
        if command[0]=="insert":
            l.insert(int(command[1]),int(command[2]))
        elif command[0]=="append":
            l.append(int(command[1]))
        elif command[0]=="remove":
            l.remove(int(command[1]))
        elif command[0]=="print":
            print(l)
        elif command[0]=="pop":
            l.pop()
        elif command[0]=="reverse":
            l.reverse()
        elif command[0]=="sort":
            l.sort()
