# find 함수
a = "Python is the best choice"
print(a.find("b"))
print(a.find("P"))
print(a.find("k"))

# index 함수
b = "Life is too short"
print(b.index("t"))

# join 함수
print(",".join("abcd"))

# replace 함수
sentence = "Life is too short"
print(sentence.replace("Life", "Your leg"))

# 삼중리스트 인덱싱하기
triple_list = [1, 2, ["a", "b", ["Life", "is"]]]

# Life 인덱싱 하기
print(triple_list[2][2][0])

# list와 tuple의 차이 :
# 1) [] / ()
# 2) list는 수정 가능 / tuple은 수정 불가능

# dictionary
dict = {"name": "seungah", "phone": "30990291", "birth": {"0318", "0214"}}
print(dict["birth"])

# dictionary 함수 key

dict_key = {"name": "seungah", "phone": "010-3099-0291", "birth": "1989-03-18"}
print(dict_key.keys())
