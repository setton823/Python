my_friends = ["山田", "田中", "中山", "山内"]
type(my_friends)
my_friends[0] = ["田んぼの田"]
a = [1, 2, 3]
b = [4, 5, 6]
c = [a, b]
c = [[1, 2, 3], [4, 5, 6]]      #ネストされたリスト
c = [0][2]
3
a = [0, 1, 2, 3, 4]
len(a)
5
a = ["a", "b", "c"]
a.append(4)
a
["a", "b", "c", "4"]
a.insert(0, "z")
a
["z", "a", "b", "c", "4"]
a.pop()     #pop : 最後の要素を取り出すメソッド(順番を指定)
4
a
["z", "a", "b", "c"]
a.pop(0)
"z"
a
["a", "b", "c"]
a.remove("a")       #remove : データそのものを指定して取り出すメソッド
a
["b", "c"]
num_list = [20, 50, 33, 77, 15]
num_list.sort()     #sort : 昇順に並べる    #sort(reverse=True) : 降順に並べる
num_list
[15, 20, 33, 50, 77]
77 in num_list
True
100 in num_list
False
name_list = ["My", "name", "is", "Ken"]
name_list 
['My', 'name', 'is', 'Ken']
' '.join(name_list)     #join : リストの中の文字列を指定した文字で繋ぐ
'My name is Ken'
'My name is Ken'.split()        #split : リストの中の文字列を分割する
['My', 'name', 'is', 'Ken']    
