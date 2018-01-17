#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 15:45:04 2018

@author: wangcarlos
"""
#                       -----------
# ---------------------|CSV to SHP |------------------------
#                       -----------

import pandas as pd
import ogr
import osr

Passed_line = pd.read_csv('Passed_line.csv')

X_a = Passed_line['X_Start']
Y_a = Passed_line['Y_Start']
X_b = Passed_line['X_End']
Y_b = Passed_line['Y_End']

# set up the shapefile driver
ds = ogr.GetDriverByName('ESRI Shapefile')

# create the data source
Path = "Path.shp"
data_source = ds.CreateDataSource(Path)

# create the spatial reference, WGS84
srs = osr.SpatialReference()
srs.ImportFromEPSG(4326)

# create the layer
layer = data_source.CreateLayer("data", srs, ogr.wkbMultiLineString)

# add features to shapfile 
i = list(range(0,46,1))
for x1, y1, x2, y2 in zip(i,i,i,i):
    # create the feature
    feature = ogr.Feature(layer.GetLayerDefn())
    
    # create start and end points
    x_a = X_a[x1]
    y_a = Y_a[y1]
    x_b = X_b[x2]
    y_b = Y_b[y2]
    
    # create multiline
    multiline = ogr.Geometry(ogr.wkbMultiLineString)
    
    # add points to line 
    line = ogr.Geometry(ogr.wkbLineString)
    line.AddPoint(x_a, y_a)
    line.AddPoint(x_b, y_b)
    multiline.AddGeometry(line)
    #print(multiline.ExportToWkt())
    
    # Set the feature geometry using the multiline
    feature.SetGeometryDirectly(multiline)
    
    # Create the feature in the layer (shapefile)
    layer.CreateFeature(feature)

# Save and close the data source  
data_source = None