# MATLAB Readme

This script to generates plots to compare sensor data of wolf and sheep with their respective generated paths for specified trial(s).

Requires:
* CSV output from generate_trials.py + their filepaths
    * ws_pairs.csv
    * Sphero{x}_p2m_points.csv, where x = number associated that specific Sphero i.e. Sphero1 

Notes:
* Sphero sensor data CSVs need to be edited s.t. all cells only contain numbers. 
* Trials that will be plotted are specified using the array toGraph in line 17
* Figures are automatically saved to current working directory. To disable, comment out line 88. 
