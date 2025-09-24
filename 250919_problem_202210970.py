"""
요세푸스 문제는 다음과 같다.

1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오"""
import sys
from collections import deque
def postive_int():
    while True:
        s = input("N과 K를 입력하세요 : ").strip()
        parts = s.split()
        if len(parts) != 2:
            print(" 두 개의 값을 공백으로 구분해 입력하세요. : ")
            continue

        a, b = parts

        # isdigit(): 음수, 소수점, 지수, 허수, 기호 등 모두 거부
        if not (a.isdigit() and b.isdigit()):
            print("숫자 이외의 문자가 포함되었습니다. 양의 정수만 입력하세요.")
            continue

        N, K = int(a), int(b)

        if N <= 0 or K <= 0:
            print("0 또는 음수는 허용되지 않습니다. 양의 정수만 입력하세요.")
            continue

        if K > N:
            print("K는 N보다 클 수 없습니다. (조건: K ≤ N)")    
            continue

        return N, K
def josephus(n,k): #n: 사람 수, k: 제거 간격
    q = deque(range(1, n + 1))
    aws = []

    while q:
        q.rotate(-k + 1)  # K-1칸 앞으로 이동
        aws.append(q.popleft())  # K번째 사람 제거

    return aws
def main():
    N, K = postive_int()
    result = josephus(N, K)
    print("<" + ", ".join(map(str, result)) + ">")

if __name__ == "__main__":
    main()
