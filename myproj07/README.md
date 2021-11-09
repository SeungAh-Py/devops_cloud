# 교육 7일차(예시)

## 파이썬 map

목록으로부터 값을 하나씩 받아서 변환하여, 새로운 목록을 생성

```python
def make_power(nubmer):
    return number ** 2

for number in map(makea_power, range(1, 10)):
    print(number)
```