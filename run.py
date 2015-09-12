#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "Osman Baskaya"

from graphcommons import GraphCommons

api = GraphCommons('sk_mZuW-l1lWAeMb17wlwPn0g')
print api.status()

def create_edge(from_node, to_node, relation_type, to_type, from_type):

    base = [("action", "edge_create"), 
            ("from_name", from_node), 
            ("from_type", from_type), 
            ("to_name", to_node), 
            ("to_type", to_type), 
            ("name", relation_type), 
            ("properties", {})]

    return dict(base)


def create_node(from_node, to_node, relation_type, to_type, from_type):

    base = [("action", "edge_create"), 
            ("from_name", from_node), 
            ("from_type", from_type), 
            ("to_name", to_node), 
            ("to_type", to_type), 
            ("name", relation_type), 
            ("properties", {})]

    return dict(base)
