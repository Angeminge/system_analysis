import csv


def task(graph: str) -> list:
    ansv = [[], [], [], [], []]

    reader = csv.reader(graph.split('\n'))
    edges = []
    for edge in reader:
        node1, node2 = map(int, edge)
        edges.append((node1, node2))
        ansv[0].append(node1)  # r1
        ansv[1].append(node2)  # r2

    for edge in edges:
        node1, node2 = edge
        if node2 in ansv[0]:
            ansv[2].append(node1)  # r3
        if node1 in ansv[1]:
            ansv[3].append(node2)  # r4
        if ansv[0].count(node1) > 1:
            ansv[4].append(node2)  # r5

    return [list(set(i)) for i in ansv]