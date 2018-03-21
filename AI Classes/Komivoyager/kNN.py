import math
import csv


def data_getter():
    points = []
    with open('/home/slawek/PycharmProjects/kNN/test2.csv', 'r') as file:
        data = csv.reader(file, delimiter=',')
        for row in data:
            x, y = int(row[0]), int(row[1])
            points.append([x, y])
        return points


def compute_dist(lst, start):
    add_1 = 0
    iterationResults = []
    for elem in lst:
        while add_1 < len(lst):
            if add_1 != start:
                result = round(math.sqrt((math.pow((lst[start][0] - lst[add_1][0]), 2)) +
                            (math.pow((lst[start][1] - lst[add_1][1]), 2))), 2)
                iterationResults.append(result)
                add_1 += 1
            else:
                iterationResults.append('x')
                add_1 += 1
    return iterationResults


def new_index(lst, element):
    for position, item in enumerate(lst):
        if item[:2] == element[:2]:
            return position


def start_and_dist(lst):
    nlist = list(filter(lambda arr: 'x' not in arr, lst))
    dist = min(list(map(lambda arr: arr[-1], nlist)))
    new_start = [x[:2] for x in nlist if x[-1] == dist][0]
    return dist, new_start


def way_back(lst):
    return round(math.sqrt((math.pow((lst[0][0] - lst[len(lst)-1][0]), 2)) +
                            (math.pow((lst[0][1] - lst[len(lst)-1][1]), 2))), 2)

def zalegla(lst):
    x = lst[0]
    return lst.append(x)


def main():
    start = int(input("Set the travel start point: "))
    start -= 1
    total = 0
    data = data_getter()
    been = []
    for ele in data:
        if data.index(ele) == 0:
            for ele in data:
                ele.append(compute_dist(data, start)[data.index(ele)])
            been.extend([x[:2] for x in data if isinstance(x[-1], str)])
            total += start_and_dist(data)[0]
        else:
            start = new_index(data, start_and_dist(data)[1])
            for ele in data:
                ele.append(compute_dist(data, start)[data.index(ele)])
            been.extend([x[:2] for x in data if isinstance(x[-1], str)])
            try:
                total += start_and_dist(data)[0]
            except ValueError:
                pass
    total += way_back(been)
    print(zalegla(been))
    print('Total distance is: ', round(total, 2))
    print('The route is: ', been)



if __name__ == "__main__":
    main()
