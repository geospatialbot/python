# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Append_Recreate_Spatial_Index.py
# Created on: 2014-09-09 11:48:37.00000
#   (generated by ArcGIS/ModelBuilder)
# Description: 
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy


# Local variables:
Boxes_4 = "Database Connections\\SDE@Canada.sde\\Canada.SDE.Boxes_4"
Boxes_2 = "Database Connections\\SDE@Canada.sde\\Canada.SDE.Boxes_2"
Boxes_2_updated = "Database Connections\\SDE@Canada.sde\\Canada.SDE.Boxes_2"

# Process: Append
arcpy.Append_management("'Database Connections\\SDE@Canada.sde\\Canada.SDE.Boxes_4'", Boxes_2, "TEST", "", "")

# Drop spatial index


# Process: Add Spatial Index
arcpy.AddSpatialIndex_management(Boxes_2_updated, "-6", "0", "0")

