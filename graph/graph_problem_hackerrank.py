#!/bin/python

'''
https://www.hackerrank.com/challenges/torque-and-development
'''

import sys

def find_city_with_max_connections(city_map):
    city_count = (-1, -1)
    for i in city_map:
        if city_map[i] > city_count[0]:
            city_count = (city_map[i], i)
    return city_count

def find_key(k,passed_value):
    for key, value in k.iteritems():
        if value == passed_value:
            return key
    return None

q = int(raw_input().strip())
for a0 in xrange(q):
    n, m, x, y = raw_input().strip().split(' ')
    n, m, x, y = [int(n), int(m), long(x), long(y)]
    city_map = {}
    city_visit = set()
    cost_library = n * x
    cost_repair = x
    if x <= y:
        print cost_library
        continue
    for a1 in xrange(m):
        city_1, city_2 = raw_input().strip().split(' ')
        city_1, city_2 = [int(city_1), int(city_2)]
        if city_1 in city_map.values():
            key = find_key(city_map, city_1)
            city_map[key].append(city_2)
        if city_2 not in city_map.keys():
            city_map[city_1] = city_map.get(city_1, [])
            city_map[city_1].append(city_2)
        else:
            city_map[city_2].append(city_1)
    max_city = find_city_with_max_connections(city_map)
    city_visit.add(max_city[1])

    for j in city_map[max_city[1]]:
        if j not in city_visit:
          cost_repair += y
          city_visit.add(j)
    for i in city_map:
        if i not in city_visit:
           cost_repair += y
           city_visit.add(j)
    print cost_repair
