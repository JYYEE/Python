# for문
# 수학적 규칙성이 존재하면 반복문을 돌릴 수 있지만 문자열은 규칙성이 존재하지 않기 때문에 배열 안에다가 넣어주고 반복문 돌리기.
arr = ["김지완", "이지영", "신현근"]

for idx, i in enumerate(arr) : 
    print(idx, i)

# enumerate : index까지 같이 확인할 수 있음. 
