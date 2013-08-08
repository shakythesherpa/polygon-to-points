polygon-to-points
=================
This script is for converting polygon landuse polygon features in a shapefile that are attributed as settlements into a points. 

The following are the steps involved:

1. Import the tileset with shapefiles (need to iterate through the folder structure)
2. Select the landuse layer from the list of shapefiles
3. Sub-select the settlement areas from the landuse layer
4. Calculate the area of the settlement areas
5. Convert the polygon settlement areas into points
6. Save the points within each tile folder


The following are the steps to merge and spatially join the points to respective admin boundaries

1. Import the point shapefiles (need to iterate through the folder structure)
2. Read the points as a list of input files as part of a list
3. Merge all the points and save as a new set of point 
4. Calculate the XY Coordinates of the points(Use Decimal Degrees same as the Dataframe)
5. Spatial join the admin boundaries for assigning the attributes(Use points as source and polygon as target vectors)


The following steps are to post-process the attribute data to calculate settlement population

1. Summarize the above join output by name of the admin unit
2. Join the summary table to the new join output layer
3. Calculate the area ratio for each cluster point (Area of cluster/Sum of Cluster Area)
4. Calculate the population/households using the above ratio
