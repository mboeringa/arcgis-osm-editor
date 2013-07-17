import arcpy
from arcpy import env

# load the standard OpenStreetMap bpx as it references the core OSM tools
arcpy.ImportToolbox(r'C:\Program Files\ESRI\OSMEditor\Data\OpenStreetMap Toolbox.tbx')

# define the enterprise geodatabase workspace
env.workspace = r'C:\Data\OSM\Mxds\osmsdeconn.sde'

# get the start date/time for synchronization (first parameter)
start_diff_time = arcpy.GetParameterAsText(0)

# load only diffs inside the AOI
load_inside_aoi = arcpy.GetParameter(1)

# name of feature dataset to synchronize
inputName = arcpy.GetParameterAsText(2)

validatedTableName = arcpy.ValidateTableName(inputName, env.workspace)
# combine name of workspace and dataset
syncDatasetName = arcpy.os.path.join(env.workspace, inputName)

arcpy.AddMessage(syncDatasetName)

try:
    arcpy.OSMGPCombineAttributes_osmtools(arcpy.os.path.join(syncDatasetName, inputName + "_osm_ply"),"osm_addr_58_country;osm_addr_58_city;osm_source;osm_source_58_name")
    
    # retrieve the deltas from the OpenStreetMap server and load them into the local geodatabase
    arcpy.OSMGPDiffLoader_osmtools(r'#',syncDatasetName,start_diff_time,load_inside_aoi,'NORMAL_LOGGING')

except:
    pass

# Return the resulting messages as script tool output messages
#
x = 0
while x < arcpy.GetMessageCount():
    arcpy.AddReturnMessage(x)
    x = x + 1
