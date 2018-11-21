import arcpy
mxd = arcpy.mapping.MapDocument(r"C:\EditingTemplates\UtilityNetworkEditingA4W\MapsandGeodatabase\Copy_of_WaterUtilityNetworkEditing.mxd")
#Update label classes
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.supports("LABELCLASSES"):
        for lblClass in lyr.labelClasses:
            lblClass.SQLQuery = lblClass.SQLQuery.replace('"', '')
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.supports("LABELCLASSES"):
        for lblClass in lyr.labelClasses:
            lblClass.SQLQuery = lblClass.SQLQuery.replace("SHAPE_Length", "Shape.STLength()")
for lyr in arcpy.mapping.ListLayers(mxd):
    if lyr.supports("LABELCLASSES"):
        for lblClass in lyr.labelClasses:
			lblClass.SQLQuery = lblClass.SQLQuery.replace("SHAPE_Area", "SHAPE.STArea()")
#Update query definitions  
for lyr in arcpy.mapping.ListLayers(mxd):  
    if lyr.supports("definitionQuery"):  
       lyr.definitionQuery = lyr.definitionQuery.replace('"', '')  
       lyr.definitionQuery = lyr.definitionQuery.replace("SHAPE_Length", "Shape.STLength()")
for lyr in arcpy.mapping.ListLayers(mxd):  
    if lyr.supports("definitionQuery"):
	   lyr.definitionQuery = lyr.definitionQuery.replace("SHAPE_Area", "SHAPE.STArea()")	   
mxd.saveACopy(r"C:\EditingTemplates\UtilityNetworkEditingA4W\MapsandGeodatabase\Copy_of_WaterUtilityNetworkEditing4.mxd")
del mxd