def colMovingAverage():
    sum = 0
    count = 0
    avg = 0
    while True:
        num = yield avg
        sum += num
        count += 1
        avg = sum / count

avg_g = colMovingAverage()
avg_g.__next__()
average = avg_g.send(1)
average = avg_g.send(3)
average = avg_g.send(5)
print(average)
