
from re import I


def factorize(num):
    output = ""
    for i in range(2, num):
        if ((num%i)==0):
            output += str(i) + " "
            num=num/i
    print(output)

def queen(n, m, x, y):
    board=[[0 for i in range(m)] for j in range(n)]
    board[y][x]=2
    for i in range(n):
        if (board[i][x]!=2):
            board[i][x]=1
    for i in range(m):
        if (board[y][i]!=2):
            board[y][i]=1
    for i in range(y):
        if (y-1-i>=0):
            if (x-1-i>=0):
                board[y-1-i][x-1-i]=1
            if (x+i+1<m):
                board[y-1-i][x+i+1]=1
    for i in range(n-y-1):
        if (y+1+i>=0):
            if (x-1-i>=0):
                board[y+i+1][x-i-1]=1
            if (x+i+1<m):
                board[y+i+1][x+i+1]=1
    
    for i in range(n):
        str=""
        for j in range(m):
            if (board[j][i]==0):
                str+="."
            elif (board[j][i]==1):
                str+="*"
            else:
                str+="D"
        print(str)

def censor_number(n, k):
    for i in range(n):
        if (str(i+1).__contains__(str(k))):
            print("*")
        else:
            print(str(i+1))

def text_analysis(path):
    f = open(path, "r", encoding='utf-8-sig')
    text=f.read()
    f.close()
    s=text.lower()
    chars = {}
    #print("test1")
    for i in s:
        if (chars.__contains__(i)):
            num=chars.__getitem__(i)+1
            chars.update({i: num})
        else:
            chars.update({i: 1})
    
    words = {}
    w=""
    #enter=0
    #print("test2")
    for i in s:
        if (i != ' ') and (i!='\n'):
            w+=i
        elif (words.__contains__(w)):
            num=words.__getitem__(w)+1
            words.update({w: num})
            w=""
            #enter=0
        else:
            words.update({w: 1})
            w=""
            #enter=0
    return words

def get_words(N, M, words):
    a = {k:words[k] for k in words if len(k)>=M}
    for i in range(N):
        word=max(a, key=a.get)
        print(word + " " + str(a[word]))
        del a[word]

def cypher(input, output):
    f = open(input, "r", encoding='utf-8-sig')
    text=f.read()
    f.close()
    r_off=10
    out=""
    for i in text:
        num=ord(i)
        if (num>=65) and (num<=90):
            num=num+r_off
            if (num>90):
                num=num-26
        elif (num>=97) and (num<=122):
            num=num+r_off
            if (num>122):
                num=num-26
        out+=chr(num)
    w = open(output, "w", encoding='utf-8-sig')
    w.write(out)
    w.close()

def decypher(input):
    f = open(input, "r", encoding='utf-8-sig')
    text=f.read()
    f.close()
    r_off=10
    out=""
    for i in text:
        num=ord(i)
        if (num>=65) and (num<=90):
            num=num-r_off
            if (num<65):
                num=num+26
        elif (num>=97) and (num<=122):
            num=num-r_off
            if (num<97):
                num=num+26
        out+=chr(num)
    print(out)


if __name__ == "__main__":
    #factorize(21)
    #queen(8, 8, 4, 3)
    censor_number(23, 2)
    #text_analysis("book.txt")
    #get_words(3, 10, text_analysis("book.txt"))
    #cypher("book.txt", "cypher.txt")
    #decypher("cypher.txt")
