#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

from graphcommons import GraphCommons, Signal
import argparse
import dataread
from itertools import chain

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

    return dict(base)
    


def create_empty_graph(api, graph_name, description=""):

    graph = api.new_graph(name=graph_name, description=description)
    return graph.id


def update_graph(api, graph_id, signals):
    print "Updating graph %s" % graph_id
    api.update_graph(id=graph_id, signals=signals)


def create_from_txt(api, input_file, graph_id=None):

    journalists, newspapers, reasons, edges = dataread.parsetsv(input_file)
    if graph_id is None:
        graph_id = create_empty_graph(api, "Fired Journalists")
        print "Graph created: {}".format(graph_id)

    print "Processing {}".format(graph_id)
    
    signals = []
    total_num_node = 0
    for element in chain(journalists, newspapers, reasons):
        node = create_node(**dict(element))
        signals.append(Signal(**node))
        total_num_node += 1

    print "Total # of node: %d" % total_num_node

    update_graph(api, graph_id, signals)
    
    signals = []
    for element in edges:
        edge = create_edge(**dict(element))
        signals.append(Signal(**edge))
    
    update_graph(api, graph_id, signals)
    return graph_id

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--developer-key', required=True)
    parser.add_argument('--input-file', required=True)
    parser.add_argument('--graph-id')

    args = parser.parse_args()

    api = GraphCommons(args.developer_key)
    print create_from_txt(api, args.input_file)
    print api.status()

# to run this script: python run.py --developer-key <YOUR_DEV_KEY> --input-file <INPUT_FILE (tab separated file)>
