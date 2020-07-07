# parent -> node -> cost
graph = {}
# cost from start to node
costs = {}
# parent of each node
parents = {}
# already proceeded node
proceeded = []

infinity = float("inf")

graph["start"] = {}
graph["start"]["A"] = 6
graph["start"]["B"] = 6
graph["A"] = {}
graph["A"]["terminal"] = 1
graph["B"] = {}
graph["B"]["A"] = 3
graph["B"]["terminal"] = 5
graph["terminal"] = {}

costs["A"] = 6
costs["B"] = 2
costs["terminal"] = float("inf")

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # 遍历所有节点
    for node in costs:
        # 当前节点没有被处理过，且开销最小
        if lowest_cost > costs[node] and node not in proceeded:
            lowest_cost = costs[node]
            lowest_cost_node = node
    return lowest_cost_node


# 找出开销最小的节点
node = find_lowest_cost_node(costs)
while node:
    # 更新邻居的开销
    neighbors = graph[node]
    cost = costs[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    proceeded += [node]
    node = find_lowest_cost_node(costs)

print("lowest cost from start to end is %d" % costs["terminal"] )





