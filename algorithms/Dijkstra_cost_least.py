#!/usr/bin/env python
# encoding: utf-8
'''
@author: jianhan513@163.com
@time: 2020/1/26 下午4:03
'''

def dijkstra():
    """
    for calculate the lowest cost path for assets/dijkstra.jpg
    """

    graph={}
    graph["start"]={}
    graph["start"]["a"]=5
    graph["start"]["b"]=2

    graph["a"]={}
    graph["a"]["c"]=4
    graph["a"]["d"]=2

    graph["b"]={}
    graph["b"]["a"]=8
    graph["b"]["d"]=7

    graph["c"]={}
    graph["c"]["end"]=3
    graph["c"]["d"]=6

    graph["d"]={}
    graph["d"]["end"]=1

    graph["end"]={}

    costs={}
    infinity=float("inf")
    costs["a"]=5
    costs["b"]=2
    costs["end"]=infinity

    parents={}
    parents["a"]="start"
    parents["b"]="start"

    do_dijkstra(graph, costs, parents)

def do_dijkstra(graph, costs, parents):
    processed=[]
    infinity=float("inf")

    node=fine_lowest_cost_node(costs,processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for n in neighbors.keys():
            new_cost=cost+neighbors[n]
            cost_n = costs.get(n, infinity)
            if new_cost < cost_n:
                costs[n]=new_cost
                parents[n]= node
        processed.append(node)
        node = fine_lowest_cost_node(costs, processed)

    parent=parents["end"]
    parent_chain="end"
    while parent is not "start":
        parent_chain = parent + "->" + parent_chain
        parent=parents[parent]
    parent_chain = "start->"+parent_chain
    print("the lowest cost is:", costs["end"], "the path is:",parent_chain)

def fine_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node=None

    for node in costs:
        cost= costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost=cost
            lowest_cost_node=node

    return lowest_cost_node