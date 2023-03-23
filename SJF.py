def fwt(process, n ,wt):         # fwt refers to finding Waiting Time
    rt = [0] * n

    for i in range(n):
        rt[i] = process[i][1]

