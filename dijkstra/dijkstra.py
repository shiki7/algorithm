import math

route_list = [[0, 100, 20, 0, 0], [0, 0, 50, 30, 0], [0, 0, 0, 20, 75],
              [0, 0, 0, 0, 40], [0, 0, 0, 0, 0]]

N = len(route_list)

unsearched_nodes = list(range(N))  #未探索ノード
distance = [math.inf] * N
previous_nodes = [-1] * N
distance[0] = 0


def get_target_min_index(min_index, distance, unsearched_nodes):
    start = 0
    while True:
        index = distance.index(min_index, start)
        if index in unsearched_nodes:
            return index
        else:
            start = index + 1


while (len(unsearched_nodes) != 0):
    possible_min_distance = math.inf
    for node_index in unsearched_nodes:
        if possible_min_distance > distance[node_index]:
            possible_min_distance = distance[node_index]
    target_min_index = get_target_min_index(possible_min_distance, distance,
                                            unsearched_nodes)
    unsearched_nodes.remove(target_min_index)

    target_edge = route_list[target_min_index]

    for i, route_distance in enumerate(target_edge):
        if route_distance != 0 and distance[i] > (distance[target_min_index] +
                                                  route_distance):
            distance[i] = distance[target_min_index] + route_distance
            previous_nodes[i] = target_min_index

print("-----経路-----")
previous_node = N - 1
while previous_node != -1:
    if previous_node != 0:
        print(str(previous_node + 1) + " <- ", end='')
    else:
        print(str(previous_node + 1))
    previous_node = previous_nodes[previous_node]

print("-----距離-----")
print(distance[N - 1])
