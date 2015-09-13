#! /usr/bin/python
# -*- coding: utf-8 -*-
import codecs

def parsetsv(input_file):
    f = codecs.open(input_file, encoding='utf-8')
    journalists = set()
    newspapers = set()
    reasons = set()
    edges = set()
    f.readline()
    for line in f:
        line = line.strip().split('\t')
        journalists.add((('node_name', line[0]), ('node_type', "Gazeteci"), ("description", "")))
        newspapers.add((('node_name', line[1]), ('node_type', "Gazete"), ("description", "")))
        newspapers.add((('node_name', line[4]), ('node_type', "Gazete"), ("description", "")))

        if line[2] == '1':
            relation_type = "İstifa"
        else:
            relation_type = "İşten Atılma"

        reasons.add((("node_name", relation_type), ("node_type", "Sebep"), ("description", "")))
        edges.add((("from_node", line[1]), ("to_node", line[0]), ("relation_type", "Eski iş"), ("from_type", "Gazete"), ("to_type", "Gazeteci")))

        edges.add((("from_node", line[0]), ("to_node", line[4]), ("relation_type", "Yeni iş"), ("from_type", "Gazeteci"), ("to_type", "Gazete")))
        edges.add((("from_node", line[1]), ("to_node", relation_type), ("relation_type", "Eylem"), ("from_type", "Gazete"), ("to_type", "Sebep")))
    return journalists, newspapers, reasons, edges

