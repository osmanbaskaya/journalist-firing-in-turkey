#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

from graphcommons import GraphCommons, Signal
import argparse


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
    api.update_graph(id=graph_id, signals=signals)


def create_from_txt(api):
    print api
    print api.status()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--developer-key', required=True)

    args = parser.parse_args()

    api = GraphCommons(args.developer_key)
    api.status()
    create_from_txt(api)
