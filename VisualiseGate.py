import sys
import uproot
import numpy as np


# Get file path
if len(sys.argv) != 2:
  print( "Please specify GATE file to open" )
  exit()


# Helper function to fill arrays
def initOrAppend( target, events, branch ):
  if target is None:
    target = events[ branch + "1" ]
  else:
    target = np.append( target, events[ branch + "1" ] )
  target = np.append( target, events[ branch + "2" ] )
  return target


# Get position arrays and a value to use for colours
xVals = None
yVals = None
zVals = None
rVals = None
gVals = None
bVals = None
for events in uproot.iterate( sys.argv[1] + ":Coincidences" ):

  xVals = initOrAppend( xVals, events, "globalPosX" )
  yVals = initOrAppend( yVals, events, "globalPosY" )
  zVals = initOrAppend( zVals, events, "globalPosZ" )
  rVals = initOrAppend( rVals, events, "crystalID" )
  gVals = initOrAppend( gVals, events, "rsectorID" )
  bVals = initOrAppend( bVals, events, "submoduleID" )
  #visVals = initOrAppend( visVals, events, "moduleID" )


# Turn columns into 2D arrays [ [x,y,z], ... ]
# Normalise value to use for colours
coordinates = np.column_stack( [ xVals, yVals, zVals ] )
colours = np.column_stack( [ rVals / np.max( rVals ),
                             gVals / np.max( gVals ),
                             bVals / np.max( bVals ) ] )

print( xVals[0], yVals[0], zVals[0], coordinates[0], rVals[0], gVals[0], bVals[0], colours[0] )


########################
# fiducial marker
# x red y green z blue

for i in range(50):
  coordinates = np.append( coordinates, [[i,0,0]], axis=0 )
  colours = np.append( colours, [[1,0,0]], axis=0 )
  coordinates = np.append( coordinates, [[0,i,0]], axis=0 )
  colours = np.append( colours, [[0,1,0]], axis=0 )
  coordinates = np.append( coordinates, [[0,0,i]], axis=0 )
  colours = np.append( colours, [[0,0,1]], axis=0 )


########################
# visualisation boilerplate

import open3d as o3d

# Display the point cloud
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector( coordinates )
pcd.colors = o3d.utility.Vector3dVector( colours )
o3d.visualization.draw_geometries( [pcd] )
