import arcpy
arcpy.env.workspace = r"\\gisdbsvr\c$\temp\931GDB.gdb" #change to where your data is stored

fc_list = arcpy.ListFeatureClasses("COSH_Production_GISLOADER_*")

for fc in fc_list:
    new_name = fc.split("COSH_Production_GISLOADER_")[-1]
    arcpy.Rename_management(fc, new_name)
