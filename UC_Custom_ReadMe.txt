UC 2013 Customizations - Feature Service Sync to OSM with Custom Templates

What: Customized mxds for templates for Chibombo (Zambia), Cochabamba (Bolivia) and Kalingalinga (Zambia) for the 2013 OpenStreetMap Mapping Party at the Esri User Conference. Also includes customized python scripts for data upload, download, and sync through the feature service for additional OSM tags: source:name=[WorldBank project], city=[city location], country=[country] and source:DigitalGlobe.

Status: prototype; there are unresolved issues with the tags being automatically synced to OpenStreetMap

File locations:
* Mxds: Chibombo.mxd, Cochabamba.mxd, Kalingalinga.mxd
	**located in codebase here: \\arcgis-osm-editor\src\OSMWeb10_1\Mxds
	**Copy here on server machine: \\C:\Data\OSM\Mxds

* Python scripts: svr_datadownload.py, svr_datasync.py, svr_dataupload.py
	**located in codebase here: \\arcgis-osm-editor\src\data
	**Copy here on server machine: \\arcgisserver\directories\arcgissystem\arcgisinput\OSM_on_AGS.GPServer\extracted\v101\data

* OSM Web config: web.config (calls mxd templates, 5 & 15 minute sync intervals, and custom message in upload comment)
	**located in codebase here: \\arcgis-osm-editor\src\OSMWeb10_1
	**Copy here on server machine: \\C:\inetpub\wwwroot\OSM

 