import arcpy, os

path = r"C:\Geo_Data\TripMaster_August2013\TM_Shape_points"




arcpy.env.workspace = path
shp = arcpy.arcpy.ListFeatureClasses()
for i in shp:
    print i
    arcpy.DefineProjection_management(os.path.join(path, i), "PROJCS['NAD_1983_StatePlane_California_V_FIPS_0405_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',6561666.666666666],PARAMETER['False_Northing',1640416.666666667],PARAMETER['Central_Meridian',-118.0],PARAMETER['Standard_Parallel_1',34.03333333333333],PARAMETER['Standard_Parallel_2',35.46666666666667],PARAMETER['Latitude_Of_Origin',33.5],UNIT['Foot_US',0.3048006096012192]]")