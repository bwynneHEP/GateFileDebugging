'''
src/IO/InputStreamFromROOTFile.cxx
  stream_ptr->SetBranchAddress("time1", &time1, &br_time1);
  stream_ptr->SetBranchAddress("time2", &time2, &br_time2);
  stream_ptr->SetBranchAddress("eventID1", &eventID1, &br_eventID1);
  stream_ptr->SetBranchAddress("eventID2", &eventID2, &br_eventID2);
  stream_ptr->SetBranchAddress("energy1", &energy1, &br_energy1);
  stream_ptr->SetBranchAddress("energy2", &energy2, &br_energy2);
  stream_ptr->SetBranchAddress("comptonPhantom1", &comptonphantom1, &br_comptonPhantom1);
  stream_ptr->SetBranchAddress("comptonPhantom2", &comptonphantom2, &br_comptonPhantom2);

Error in <TTree::SetBranchStatus>: unknown branch -> crystalID1
Error in <TTree::SetBranchStatus>: unknown branch -> crystalID2
Error in <TTree::SetBranchStatus>: unknown branch -> submoduleID1
Error in <TTree::SetBranchStatus>: unknown branch -> submoduleID2
Error in <TTree::SetBranchStatus>: unknown branch -> moduleID1
Error in <TTree::SetBranchStatus>: unknown branch -> moduleID2
Error in <TTree::SetBranchStatus>: unknown branch -> rsectorID1
Error in <TTree::SetBranchStatus>: unknown branch -> rsectorID2


src/include/stir/IO/InputStreamFromROOTFile.h
  std::int32_t eventID1, eventID2, runID, sourceID1, sourceID2;
  double time1, time2;
  float energy1, energy2, rotation_angle, sinogramS, sinogramTheta, axialPos;
  int32_t comptonphantom1, comptonphantom2;
  float globalPosX1, globalPosX2, globalPosY1, globalPosY2, globalPosZ1, globalPosZ2;
  float sourcePosX1, sourcePosX2, sourcePosY1, sourcePosY2, sourcePosZ1, sourcePosZ2;

  std::int32_t crystalID1, crystalID2;
  std::int32_t submoduleID1, submoduleID2;
  std::int32_t moduleID1, moduleID2;
  std::int32_t rsectorID1, rsectorID2;

'''


import uproot
import numpy as np

importantBranches = ["time1", "time2", "eventID1", "eventID2", "energy1", "energy2", "comptonPhantom1", "comptonPhantom2",
                     "crystalID1", "crystalID2", "submoduleID1", "submoduleID2", "moduleID1", "moduleID2", "rsectorID1", "rsectorID2"]

outputFile = uproot.recreate( "root_data_test1.root" )
outputFile.mktree( "Coincidences", { "time1": np.float64,
                                     "time2": np.float64,
                                     "eventID1": np.int32,
                                     "eventID2": np.int32,
                                     "energy1": np.float32,
                                     "energy2": np.float32,
                                     "comptonPhantom1": np.int32,
                                     "comptonPhantom2": np.int32,
                                     "crystalID1": np.int32,
                                     "crystalID2": np.int32,
                                     "submoduleID1": np.int32,
                                     "submoduleID2": np.int32,
                                     "moduleID1": np.int32,
                                     "moduleID2": np.int32,
                                     "rsectorID1": np.int32,
                                     "rsectorID2": np.int32 })

for events in uproot.iterate( "../pretest_output/root_data_test1.root:Coincidences" ):
  
  # Eventwise - slow
  #for event in events:
  #  for branch in importantBranches:
  #    print( branch, event[branch] )

  # Batchwise - fast
  #for branch in importantBranches:
  #  print( branch, events[branch] )

  outputFile[ "Coincidences" ].extend( events[ importantBranches ] )
