def find_cycle(tasks):
    def _find_cycle(curr, tasks, exploring, finished):
        if curr not in finished and curr in exploring:
            return True

        exploring.add(curr)
        for t in tasks.get(curr, []):
            if t not in finished:
                test = _find_cycle(t, tasks, exploring, finished)
                if test: return True
        finished.add(curr)
        return False

    exploring = set()
    finished = set()
    for t in tasks:
        if t not in finished:
            test = _find_cycle(t, tasks, exploring, finished)
            if test: return True
    return False

def build(curr_task, tasks, queue, visited):
    if curr_task in visited: return
    visited.add(curr_task)
    for next in tasks.get(curr_task, []):
        build(next, tasks, queue, visited)
    queue.append(curr_task)

def helper(tasks, queue):
    visited = set()

    for t in tasks:
        build(t, tasks, queue, visited)

def solution(tasks):
    if find_cycle(tasks):
        return []

    queue = []
    helper(tasks, queue)
    return queue

def test():
    assert solution({
        'a': ['b', 'c'],
        'b': ['c', 'd'],
        'd': ['c'],
    }) == ['c', 'd', 'b', 'a']

    assert solution({'a': ['b'], 'b': ['a']}) == []

    assert solution({'a': ['b'], 'b': ['c'], 'c': ['a', 'd']}) == []

test()
