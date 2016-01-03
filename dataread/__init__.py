#! /usr/bin/python
# -*- coding: utf-8 -*-
import codecs
import pandas as pd
import datetime


def parsetsv(input_file):
    f = codecs.open(input_file, encoding='utf-8')
    journalists = set()
    newspapers = set()
    edges = set()
    f.readline()
    for line in f:
        line = line.strip().split('\t')
        journalists.add((('node_name', line[0]), ('node_type', "Journalist"), ("description", "")))
        newspapers.add((('node_name', line[1]), ('node_type', "Journal"), ("description", "")))
        newspapers.add((('node_name', line[4]), ('node_type', "Journal"), ("description", "")))

        reasons.add((("node_name", relation_type), ("node_type", "Sebep"), ("description", "")))
        edges.add((("from_node", line[1]), ("to_node", line[0]), ("relation_type", "Eski iş"), ("from_type", "Gazete"), ("to_type", "Gazeteci")))

        edges.add((("from_node", line[0]), ("to_node", line[4]), ("relation_type", "Yeni iş"), ("from_type", "Gazeteci"), ("to_type", "Gazete")))
        edges.add((("from_node", line[1]), ("to_node", relation_type), ("relation_type", "Eylem"), ("from_type", "Gazete"), ("to_type", "Sebep")))
    return journalists, newspapers, reasons, edges


def get_data(input_file, sep='\t'):
    media_df = pd.read_csv("media_types.tsv", sep='\t')
    media_type = dict(zip(media_df.MediaEntity, media_df.Type))
    
    df = pd.read_csv(input_file, sep=sep)
    journalists = set()
    newspapers = set()
    edges = set()
    nrow, ncol = df.shape
    for i in xrange(nrow):
        journalists.add((('node_name', df.Name[i]), ('node_type', "Journalist"), 
                         ("description", "{}\n{}".format(df.Job[i], df.Source2[i]))))

        newspaper1 = df.From_Where[i]
        newspaper2 = df.To_Where[i]

        newspapers.add((('node_name', newspaper1), ('node_type', media_type[newspaper1]), 
                        ("description", "")))
        newspapers.add((('node_name', newspaper2), ('node_type', media_type[newspaper2]), 
                        ("description", "")))

        leaving_date = datetime.datetime.strptime(df.Time[i], "%m/%d/%Y").year

        edges.add((("from_node", newspaper1), ("to_node", df.Name[i]), ("relation_type", "LEFT FROM"), ("from_type", media_type[newspaper1]), ("to_type", "Journalist"), ("properties", ("leaving_date", leaving_date))))

        edges.add((("from_node", df.Name[i]), ("to_node", newspaper2), ("relation_type", "HIRED"), ("from_type", "Journalist"), ("to_type", media_type[newspaper2])))

    return journalists, newspapers, edges

