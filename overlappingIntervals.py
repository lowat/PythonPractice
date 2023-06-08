def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key = lambda x: x[0])
    mergedIntervals = []
    ongoingRange = sortedIntervals[0]
    for i in range(1, len(sortedIntervals)):
        if sortedIntervals[i][0] <= ongoingRange[1]:
            ongoingRange[1] = max(sortedIntervals[i][1], ongoingRange[1])
        else:
            mergedIntervals.append(ongoingRange)
            ongoingRange = sortedIntervals[i]
    mergedIntervals.append(ongoingRange)
    return mergedIntervals