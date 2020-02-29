# -*- coding: utf-8 -*-
'''
Задание 7.1

Аналогично заданию 4.6 обработать строки из файла ospf.txt
и вывести информацию по каждой в таком виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

file = open('ospf.txt', 'r')

for line in file:
    ospf_route = line.split()
    print(''' 
        Protocol:              {}SPF
        Prefix:                {}
        AD/Metric:             {}
        Next-Hop:              {}
        Last update:           {}
        Outbound Interface:    {}'''.format(ospf_route[0],
                                            ospf_route[1],
                                            ospf_route[2].strip('[]'),
                                            ospf_route[4].replace(',', ''),
                                            ospf_route[5].replace(',', ''),
                                            ospf_route[6]))
