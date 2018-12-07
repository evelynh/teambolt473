#README for GenerateTrials

The GenerateTrials folder consists of 4 files:
* generate_csv.py
    * Used to store results of paths.py and generate_wolf.py into CSV files with correct format that MATLAB code uses to plot geneerated paths (see Matlab folder)
* paths.py
   * Code used to generate the intial points array (an array of array of points, where each array of points = points that robot should go to in a given trial) 
* generate_wolf.py
    * Code used to generate the wolf's path based on the sheep's path 
* generate_trials.py
   * Script for generating trials. For ease of use, run script and redirect output into text file with name of your choosing. 
   * Output constists of:
       * List of trials with chasing, and for each trial, what the wolf-sheep pairs is, what the offset between the wolf and the sheep is, and what the chasing subtlety is
       * Points array for each Sphero. This is the array that is copied into Broadcaster.js or Listener.js
       * Points array for each Sphero, but outputted in a more easily readible format i.e. each array is labelled with corresponding trial number