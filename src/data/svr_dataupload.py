import arcpy
from arcpy import env

# load the standard OpenStreetMap bpx as it references the core OSM tools
arcpy.ImportToolbox(r'C:\Program Files\ESRI\OSMEditor\Data\OpenStreetMap Toolbox.tbx')

# define the enterprise geodatabase workspace
env.workspace = r'C:\Data\OSM\Mxds\osmsdeconn.sde'

# name of feature dataset to synchronize
inputName = arcpy.GetParameterAsText(0)

validatedTableName = arcpy.ValidateTableName(inputName, env.workspace)
revisionTableName = arcpy.os.path.join(env.workspace,validatedTableName + '_osm_revision')

# comment describing the upload feature dataset
upload_comment = arcpy.GetParameterAsText(1)

# OSM Server login credentials (username and password)
osm_credentials = arcpy.GetParameterAsText(2)

# set tags from osm_field values
polygonFC = arcpy.os.path.join(env.workspace, validatedTableName, validatedTableName + '_osm_ply')
arcpy.OSMGPCombineAttributes_osmtools(polygonFC, "osm_addr_58_country;osm_addr_58_city;osm_source;osm_source_58_name")

# retrieve the deltas from the OpenStreetMap server and load them into the local geodatabase
arcpy.OSMGPUpload_osmtools(r'http://www.openstreetmap.org',revisionTableName,upload_comment,'OSMCHANGE_FORMAT',osm_credentials)
