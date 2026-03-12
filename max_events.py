"""Task 2"""

def max_events(inputt: str) -> int:
    """
    Calculate the maximum number of non-overlapping events that can be scheduled.
    """

    if not inputt:
        return 0

    events = inputt.split()
    intervals = []

    for event in events:
        _, time = event.split(":")
        start, end = map(int, time.split("-"))
        intervals.append((start, end))

    intervals.sort(key=lambda x: x[1])
    counter = 0
    last_end_time = -1

    for start, end in intervals:
        if start >= last_end_time:
            counter += 1
            last_end_time = end

    return counter

if __name__ == "__main__":
    s1 = "pyramids:1-5 rome:2-4 renaissance:5-8 revolution:6-9"
    assert max_events(s1) == 2

    s2 = "a:1-3 b:3-5 c:5-10"
    assert max_events(s2) == 3

    s3 = "a:1-10 b:2-3 c:4-5 d:6-7"
    assert max_events(s3) == 3

    s4 = "a:1-3 b:2-4 c:4-6 d:6-7"
    assert max_events(s4) == 3

    assert max_events("") == 0

    print("All tests passed!")
