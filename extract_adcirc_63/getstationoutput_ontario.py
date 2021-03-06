# coding: utf-8
#Extracts hydrographs from all .63 files in directory folder starting at current directory
def main():
  #import modules
  import os
  import subprocess
  #Locate executable and input files
  PARENT_DIRECTORY     = "P:/02/NY/Monroe_36055C/STUDY__TO90/TECHNICAL/ENG_FLOOD_HAZ_DEV/COASTAL/WAVE_MODELING/CSHORE_J/Hydrographs/input/"
  getstationoutput_exe = "C:/Users/jdorvinen/Desktop/cshore/getstationoutput9.exe"
  stationfile          = "C:/Users/jdorvinen/Desktop/cshore/stationfile.txt"
  stormlist            = ["C:/Users/jdorvinen/Desktop/cshore/stormslist1.txt",
                          "C:/Users/jdorvinen/Desktop/cshore/stormslist2.txt",
                          "C:/Users/jdorvinen/Desktop/cshore/stormslist3.txt",
                          "C:/Users/jdorvinen/Desktop/cshore/stormslist4.txt",
                          "C:/Users/jdorvinen/Desktop/cshore/stormslist5.txt"] ##getstationoutput_scripted.py eliminates the need for this.
  datafiles_directory  = "P:/02/LakeOntario/Storm/"
  output_directory     = "P:/02/NY/Monroe_36055C/STUDY__TO90/TECHNICAL/ENG_FLOOD_HAZ_DEV/COASTAL/WAVE_MODELING/CSHORE_J/Hydrographs/ouput"
  #call subprocess

  subprocess.Popen([getstationoutput_exe,
                    stationfile,
                    stormlist[0],
                    datafiles_directory,
                    output_directory])
  subprocess.Popen([getstationoutput_exe,
                    stationfile,
                    stormlist[1],
                    datafiles_directory,
                    output_directory])
  subprocess.Popen([getstationoutput_exe,
                    stationfile,
                    stormlist[2],
                    datafiles_directory,
                    output_directory])
  subprocess.Popen([getstationoutput_exe,
                    stationfile,
                    stormlist[4],
                    datafiles_directory,
                    output_directory])
  subprocess.Popen([getstationoutput_exe,
                    stationfile,
                    stormlist[5],
                    datafiles_directory,
                    output_directory])
if __name__ == '__main__':
  main()
