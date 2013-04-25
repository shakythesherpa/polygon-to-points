# ---------------------------------------------------------------------------
# Bako_Landuse_analysis.py
# Created on: 2012-12-05 11:52:29.00000
# Author: Shaky Sherpa
# Description:
"""
This script is used to select the settlement areas from the landuse dataset and convert them into points
"""
# ---------------------------------------------------------------------------

# Set the necessary product code and required imports


import time
# Records the starting time of the process
start_time = time.time()

#import all the necessary modules
#import arcpy
import sys
import traceback
import os
import fnmatch
import shapely
from osgeo import ogr
import ogr
from shapely.geometry import *



def folder_file_iter(root, file_match):
    # get a list of the folders under the root directory
    folders = os.walk(root).next()[1]
    #Iterate through each folder
    for folder in folders:
        full_folder = os.path.join(root, folder)
        #Get the matching file from each folder
        for filename in fnmatch.filter(os.listdir(full_folder), file_match):
            yield folder,full_folder, filename


for foldername,workspace, shapefile in folder_file_iter("C:\\Users\\SSherpa\\Dropbox\\Indonesia Geospatial Analysis\\Data Collection - Field\\BAKOSURTANAL_Land-use_maps\\MAP for Mr.Jonathan", "*5AR.shp"):

    #arcpy.env.workspace=workspace
    #arcpy.env.overwriteOutput = True


    # Local variables:
    #feat_class = shapefile
    feat_layer = "landuse_polygons"
    output_layer = "settlement_areas.shp"
    point_layer = foldername.replace("-","_")+"_settlement_points.shp"

          # print the number of records in the feature class
    """
    result = arcpy.GetCount_management(feat_class)
    print "Checking for feature class..."
    print "Number of features in the feature class " + feat_class + " : " + str(result)
    """
    os.chdir(workspace)
    # get the driver
    driver = ogr.GetDriverByName('ESRI Shapefile')
    # open the data source
    datasource = driver.Open(shapefile, 0)
    if datasource is None:
        print 'Could not open file'
        sys.exit(1)
    # get the data layer
    layer = datasource.GetLayer()
    # loop through the features and count them
    cnt = 0
    feature = layer.GetNextFeature()
    while feature:
        cnt = cnt + 1
        feature.Destroy()
        feature = layer.GetNextFeature()
    print 'There are ' + str(cnt) + ' features in' + ' '+ foldername + '-'+ shapefile
    # close the data source
    datasource.Destroy()

"""
# check to see if the feature layer exists; if so, delete it

if arcpy.Exists(feat_layer):
    arcpy.Delete_management(feat_layer)
arcpy.MakeFeatureLayer_management(feat_class, feat_layer)


#Create a query statement to select the settlment areas
query = '"KODE_UNSUR" = \'50102\''

# Process: Select Layer By Attribute
arcpy.SelectLayerByAttribute_management(feat_layer, "NEW_SELECTION", query)
print "Selecting features based on query...."

# print the number of records in the feature layer with query
result = arcpy.GetCount_management(feat_layer)
print "Number of features selected in the feature layer " + feat_layer + " with a query: "+ str(result)


# Process: Calculate Areas
arcpy.CalculateAreas_stats(feat_layer, output_layer)
print "Calculating Areas..."

# Process: Convert the output polygon features To Points
arcpy.FeatureToPoint_management(output_layer, point_layer, "INSIDE")
print "Converting polygon features" + feat_layer + " to point features layer " + point_layer

"""
"""
except:
    tb = sys.exc_info()[2]
    tbinfo = traceback.format_tb(tb)[0]
    pymsg = "PYTHON ERRORS:\nTraceback Info:\n" + tbinfo + "\nError Info:\n     " +        str(sys.exc_type) + ": " + str(sys.exc_value) + "\n"
    msgs = "ARCPY ERRORS:\n" + arcpy.GetMessages(2) + "\n"

    arcpy.AddError(msgs)
    arcpy.AddError(pymsg)

    print msgs
    print pymsg

    arcpy.AddMessage(arcpy.GetMessages(1))
    print arcpy.GetMessages(1)
"""
print "Time to process: %s" % (time.time() - start_time)
