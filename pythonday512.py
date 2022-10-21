from re import A


x = ("Adharsh.U")
y = ("not a super hero")
z = ("akshay")
print(x, y, z)
print(x.replace("s", "a"))
print(x.replace("a", "r"))
print(y.replace("o", "v"))
print(y.replace("n", "o"))
print(z.replace("o", "p"))
print(z.replace("i", "u"))
print(x.upper())
print(x.lower())
print(type(x))

x = "sometimes we wish that we need the most happends but in reality it wont happen so in my point view"
y = "the main thing is that what we wish is not gona happen awe have to a make something which is goona change the world"
z = 87, 800, 635, 65, 34, 13
print(x+y)
print(y)
print(z)
print(x.upper())
print(x.lower())
print(x.replace("is", "apl"))
print(x.replace("h", "ok"))
print(x.replace("s", "hn"))
print(x.replace("i", "yh"))
print(x.replace("k", "ai"))
print(x.replace("l", "po"))
print(y.upper())
print(y.lower())
print(y.replace("is", "hl"))
print(y.replace("h", "ok"))
print(y.replace("s", "hn"))
print(y.replace("i", "yh"))
print(y.replace("k", "uj"))
print(y.replace("l", "p"))
print(x.split())
print(y.split())
# boolenans
print(20580 > 789610)
print(67845 < 622487)
print(909632 > 787854)
print(672314 < 78851)
print(90964 < 96585)
print(90896412 == 567896)
print(bool('hello'))
print(bool(999))
# mylistcjgiuv
mylist = [10, 40, 758, "yashimine sinh nehra", 'yeijjd', "noy highku talented"]
print(mylist[4])
print(mylist[3])
print(mylist[-2])
print(mylist[-1])
print(mylist[4])
print(mylist[2])
print(mylist[2+1])
print(mylist[0+2])
print(mylist[0+5])
print(mylist)
mylist[1:4] = [200, 'doremon']
print(mylist)
mylist[1:4] = [67, 789, 987, 'milley johonson', 'mickey mouse', 'whyyyy']
print(mylist)
mylist = [10, 40, 758, "eren yeger", 'captian levi', "bikasu"]
mylist1 = [56, 777, 90, "galadriel", 'sauron', "durin"]
mylist1.extend(mylist)
print(mylist)
print(mylist1)
# yhj
mylist = ["ff8fufhh", "koloindinia", "koijkl"]
print(mylist)
mylist.clear()
print(mylist)
print(10+20)
print(20-12)
print(30*5)
print(30**5)
print(40/5)
print(40//2)
print(56 % 2)
a = 27
print(a)
a += 3
print(a)
a -= 8
print(a)
a = a*5
print(a)
a = a/9
print(a)
a = a//9
print(a)
a = a % 3
print(a)
print(67 == 7668)
print(67 != 7)
print(67 <= 798)
print(67 >= 718)
print(6798 < 658)
print(67 > 7608)
# logical operatirs
x = 6
print(x < 5 and x > 2)
print(x < 2 and x > 9)
print(x < 9 and x > 57)
print(x < 1 and x > 2)
print(x > 3) and (x > 1)
print(x > 3) and (x > 5)
print(not (x > 2 or x > 3))
# identify operator
a = [10, 20]
b = [10, 20]
c = a
print(a is c)
print(b is a)
print(a == b)
print(a is not b)
print(a != b)
# membership operator
a = [1, 2, 3, 4, 5, 6, 7]
print(6 in a)
print(5 in a)
print(2 in a)
print(1 in a)
print(0 in a)
print(7 in a)
print(9 in a)
