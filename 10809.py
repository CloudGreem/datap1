#10809



s = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alphabet:
    print(s.find(i), end=' ')

# find() : 문자열에서 특정 문자나 문자열이 처음으로 등장하는 위치(인덱스)를 반환
# 만약 찾는 문자나 문자열이 없으면 -1 반환
# index() : 문자열에서 특정 문자나 문자열이 처음으로 등장하는 위치(인덱스)를 반환
# 만약 찾는 문자나 문자열이 없으면 오류 발생
# 따라서 find()는 안전하게 사용할 수 있지만, index()는 예외 처리가 필요



