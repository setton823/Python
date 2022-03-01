menu = {"apple": 100, "orange": 200, "banana": 300}
menu
{'apple': 100, 'orange': 200, 'banana': 300}
menu["apple"]       #キー値で値を取得する
100
menu["banana"]
300
menu["grape"] = 400
menu
{'apple': 100, 'orange': 200, 'banana': 300, 'grape': 400}
menu["grape"]
400
menu["grape"] = 450
menu
{'apple': 100, 'orange': 200, 'banana': 300, 'grape': 450}
menu.keys()     #キー値を一覧表示
dict_keys(['apple', 'orange', 'banana', 'grape'])
menu.values()       #値を一覧表示
dict_values([100, 200, 300, 450])
menu.items()
dict_items([('apple', 100), ('orange', 200), ('banana', 300), ('grape', 450)])