"""
scope 1~100 missing one value
which one ?
"""

def solution(li):
    all_sum = sum(li)
    return 5050 - all_sum

if __name__ == "__main__":
    li = list(range(1,101))
    del li[93]
    print(solution(li))