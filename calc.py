# calc.py  ← 이 파일이 모듈
# ① 변수(상수)
PI = 3.14
# ② 함수
def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return None
    return a / b