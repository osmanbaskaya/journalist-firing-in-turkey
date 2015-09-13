#!/usr/bin/env python


"""
Todoes : Find a python module that imports and exports csv files
Generate three sets of nodes : Journalists, news outlets and reason 
For each line in the excel sheet, generate 3 edges
"""
def parsecsv(input_file):
    import csv
    f = open(input_file, "rb")
    dataarray = csv.reader(f,delimiter='\t')
    
    next(dataarray)
    
    journoslist = []
    papers = []
    paperlist = []
    edgeslist =[]
    
    for row in  dataarray:
        journoslist+= [[row[0],'Gazeteci',row[3]]]
        papers+=[row[4]]
        edgeslist+=[[row[1],'Gazete',row[0],'Gazeteci',row[2]]]
        edgeslist+=[[row[0],'Gazeteci',row[4],'Gazete','Basladi']]
    
    
    papersset=list(set(papers))
    for i in papersset:
        paperlist+=[[i,'Gazete','']]
        
    
    
    return [journoslist,paperlist,edgeslist]
    
    
   
