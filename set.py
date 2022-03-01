hands = {"グー", "グー", "グー", "チョキ", "チョキ"}
hands
{'グー', 'チョキ'}
type(hands)
<class 'set'>
len(hands)
2
list(hands)
['グー', 'チョキ']
list(hands)[0]
'グー'
list(hands)[1]
'チョキ'
set([1, 2, 3])
{1, 2, 3}
hands.add("パー")
hands
{'グー', 'チョキ', 'パー'}
hands.remove("グー")
hands
{'チョキ', 'パー'}
hands.discard("チョキ")
hands
{'パー'}
hands.add("グー", "チョキ")
hands.add("グー")
hands.add("パー")
hands
{'グー', 'パー'}
hands.add("チョキ")
hands
{'グー', 'チョキ', 'パー'}
A = {1, 2, 3}
B = {3, 4, 5}
A | B       #和集合
{1, 2, 3, 4, 5}
A & B       #積集合
{3}
C = {7, 8, 9}
A & C
set()
A - B       #差集合
{1, 2}
{1, 2, 3} - {1, 2}
{3}
{1, 2, 3} - {1, 2, 4}
{3}
(A | B) - (A & B)
{1, 2, 4, 5}
A ^ B
{1, 2, 4, 5}      
