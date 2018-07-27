# Given a decoder and a string of ints, return the number of ways you could decode the word.

def top_down(encoded, decoder, i, m={}):
    if i in m:
        return m[i]

    if i == len(encoded):
        return 1

    total = 0
    test = []
    for j in range(i, len(encoded) + 1):
        test.append(encoded[i:j])
        if encoded[i:j] in decoder:
            total += top_down(encoded, decoder, j, m)
    m[i] = total
    return total

def bottom_up(encoded, decoder):
    tracker = [0 for i in range(len(encoded) + 1)]
    tracker[0] = 1 # the empty string has 1 way to encode

    for right_i in range(len(encoded)):
        tracker_i = right_i + 1
        total = 0
        for left_i in range(right_i + 1):
            left = encoded[0:left_i]
            right = encoded[left_i:right_i + 1]

            if right in decoder:
                total += tracker[left_i]
        tracker[tracker_i] = total
    return tracker[-1]

def solution(encoded, decoder):
    return top_down(encoded, decoder, 0)

def test():
    test_1 = solution('111', {'1': 'a', '11': 'b'})
    assert test_1 == 3, test_1
    test_2 = solution('1234', dict([
        ( str(i - 96), chr(i)  ) for i in range(97, 123) # a to z
    ]))
    assert test_2 == 3, test_2
    print("all tests passed")

test()
