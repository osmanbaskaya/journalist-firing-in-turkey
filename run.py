#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

import graphcommons
from graphcommons import GraphCommons, Signal
import argparse
import cleanupcsv
import sys


def create_edge(from_node, to_node, relation_type, to_type, from_type):

    base = [("action", "edge_create"), 
            ("from_name", from_node), 
            ("from_type", from_type), 
            ("to_name", to_node), 
            ("to_type", to_type), 
            ("name", relation_type), 
            ("properties", {})]

    return dict(base)


def create_node(node_name, node_type, description=""):

    base = [("action", "node_create"), 
            ("name", node_name), 
            ("type", node_type), 
            ("description", description),
            ("properties", {})]
    


def create_empty_graph(api, graph_name, description=""):

    graph = api.new_graph(name=graph_name, description=description)
    return graph.id


def update_graph(api, graph_id, signals):
    api.update_graph(id=graph_id, signals=signals)


def create_from_txt(api,inputpar):
    print api
    print api.status()
    [journonodes,papernodes,edges]=cleanupcsv.parsecsv()
    if inputpar == 0:
        graph_id = create_empty_graph(api, "Fired Journalists")
        print graph_id 
    else:
        graph_id = inputpar
    for element in journonodes:
       
        api.update_graph(graph_id,signals=[Signal(action="node_create",name=element[0],type=element[1],description=element[2])])
        
       
    for element in papernodes:
        api.update_graph(graph_id,signals=[Signal(action="node_create",name=element[0],type=element[1],description=element[2])])

    
    for element in edges:
        api.update_graph(graph_id,signals=[Signal(action="edge_create",from_name=element[0],from_type=element[1],to_name=element[2],to_type=element[3],name=element[4])])
    
    return graph_id

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--developer-key', required=True)
    parser.add_argument('--input-file', required=True)

    args = parser.parse_args()

    api = GraphCommons(args.developer_key)
    print create_from_txt(api, args.input_file)
    print api.status()

# to run this script: python run.py --developer-key <YOUR_DEV_KEY> --input-file <INPUT_FILE (tab separated file)>
