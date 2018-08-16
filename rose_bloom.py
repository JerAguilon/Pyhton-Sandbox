'''
Given A, which is  a list of roses which day they will bloom
      K, which is the minimum length of an array of flowers
      M, which is the numer of long subarrays we want

      return the last day that the roses will be in M groups, or -1 if not possible
'''

def count_blooms(roses, K):
    i = 0
    total = 0
    while i < len(roses):
        if roses[i]:
            j = i
            while j < len(roses) and roses[j]:
                j += 1
            if j - i >= K:
                total += 1
            i = j
        else:
            i += 1
    return total


def solution(A, K, M):
    roses = [False for _ in range(len(A))]
    latest_solution = -1
    for i in range(len(A)):
        blooming_rose = A[i] - 1
        roses[blooming_rose] = True
        M_candidate = count_blooms(roses, K)
        if M_candidate == M:
            latest_solution = i + 1
    return latest_solution

def test_solution(A, K, M):
    print("A = {}".format(A))
    print("K = {}".format(K))
    print("M = {}".format(M))
    print(solution(A, K, M))

print(test_solution([1, 4, 3, 2, 5], 1, 3))  # -1
print(test_solution([1, 2, 7, 6, 4, 3, 5], 2, 2))  # 6

# also look at k empty slots
