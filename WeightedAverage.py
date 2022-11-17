points = input().split(" ")
weight = input().split(" ")

for i in range(3):
     points[i] = float(points[i])
     weight[i] = float(weight[i])

def weighted_average(points, weight):
    return "%.6f" %(sum([points[i]*weight[i] for i in range(len(points))])/sum(weight))


print(weighted_average(points, weight))