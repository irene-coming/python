# -*- coding: utf-8 -*-
# @Time    : 2020/1/27 下午12:08
# @Author  : jianhan513@163.com

'''
BFS：broadth first search
适用：朋友圈寻找芒果销售商
目的：找图中的最短路径
'''
from collections import deque

def bfs():
    graph={}
    graph["you"]=["alice","bob","claire"]
    graph["alice"]=["peggy"]
    graph["bob"]=["anuj","peggy"]
    graph["claire"]=["thom","jonny"]

    graph["peggy"]=[]
    graph["anuj"]=[]
    graph["thom"]=[]
    graph["jonny"] =[]

    do_bfs(graph,"you")

def do_bfs(graph, name):
    search_queue=deque()
    search_queue += graph[name]

    searched=[]

    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person+" is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    return False

def person_is_seller(person_name):
    print("check person:",person_name)
    return person_name[-1]=='m'
