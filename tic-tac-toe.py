def display(d):
    print()
    print((d["a1"]+"|"+d["a2"]+"|"+d["a3"]).center(8))
    print(("--------").center(8))
    print((d["b1"]+"|"+d["b2"]+"|"+d["b3"]).center(8))
    print(("--------").center(8))
    print((d["c1"]+"|"+d["c2"]+"|"+d["c3"]).center(8))
    print()
def insert(d,i):
    if i%2==0:
        print("Player 1")
        j=input("enter location:")
        d[j]="O "
    else:
        print("Player 2")
        j=input("enter location:")
        d[j]="X "
def check(d):
    if d["a1"]+d["a2"]+d["a3"]=="O O O ":
        print ("Player 1 is Winner")
        return True
    elif d["b1"]+d["b2"]+d["b3"]=="O O O ":
        print ("Player 1 is Winner")
        return True
    elif d["c1"]+d["c2"]+d["c3"]=="O O O ":
        print ("Player 1 is Winner")
        return True
    elif d["a1"]+d["b2"]+d["c3"]=="O O O ":
        print ("Player 1 is Winner")
        return True
    elif d["c1"]+d["b2"]+d["a3"]=="O O O ":
        print ("Player 1 is Winner")
        return True
    elif d["a1"]+d["b1"]+d["c1"]=="O O O ":
        print ("Player 1 is Winner")
        return True
    elif d["a2"]+d["b2"]+d["c2"]=="O O O ":
        print ("Player 1 is Winner")
        return True
    elif d["a3"]+d["b3"]+d["c3"]=="O O O ":
        print ("Player 1 is Winner")
        return True
    elif d["a1"]+d["a2"]+d["a3"]=="X X X ":
        print ("Player 2 is Winner")
        return True
    elif d["b1"]+d["b2"]+d["b3"]=="X X X ":
        print ("Player 2 is Winner")
        return True
    elif d["c1"]+d["c2"]+d["c3"]=="X X X ":
        print ("Player 2 is Winner")
        return True
    elif d["a1"]+d["b2"]+d["c3"]=="X X X ":
        print ("Player 2 is Winner")
        return True
    elif d["c1"]+d["b2"]+d["a3"]=="X X X ":
        print ("Player 2 is Winner")
        return True
    elif d["a1"]+d["b1"]+d["c1"]=="X X X ":
        print ("Player 2 is Winner")
        return True
    elif d["a2"]+d["b2"]+d["c2"]=="X X X ":
        print ("Player 2 is Winner")
        return True
    elif d["a3"]+d["b3"]+d["c3"]=="X X X ":
        print ("Player 2 is Winner")
        return True
    else:
        return False
d={"a1":"a1","a2":"a2","a3":"a3","b1":"b1","b2":"b2","b3":"b3","c1":"c1","c2":"c2","c3":"c3"}
c=False
display(d)
for i in range(0,9):
    insert(d,i)
    display(d)
    if i>=4:
        c=check(d)
    if c==True:
        break;
