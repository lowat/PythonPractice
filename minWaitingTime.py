def minimumWaitingTime(queries):
    queries.sort()
    timeWaited = 0
    queriesRan = 0
    for i in range(len(queries) - 1):
      queriesRan += queries[i]
      timeWaited += queriesRan
    return timeWaited