# file structure
# EventID ModuleID Energy Time R Phi Z
DATASET_EVENT, DATASET_MODULE, DATASET_ENERGY, DATASET_TIME, DATASET_R, DATASET_PHI, DATASET_Z = 0, 1, 2, 3, 4, 5, 6

import sys
import math
import uproot
import numpy as np


# Get file path
if len(sys.argv) != 2:
  print( "Please specify SimplePetScanner file to open" )
  exit()

coordinates=[]
colours=[]
for line in open( sys.argv[1] ):
  line = line.split()
  r = float( line[ DATASET_R ] )
  phi = float( line[ DATASET_PHI ] )
  z = float( line[ DATASET_Z ] )
  x = r * math.sin( phi )
  y = r * math.cos( phi )
  coordinates.append( [x, y, z] )
  colours.append( [0, float( line[ DATASET_MODULE ] ), 0] )

# Convert to numpy arrays
# Normalise value to use for colours
coordinates = np.array( coordinates )
colours = np.array( colours )
colours /= np.max( colours )

print( coordinates[0], colours[0] )


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
