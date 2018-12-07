#README for Sphero Code

Usage:
* Run Broadcaster.js on broadcaster robot
    * There should be 1 Broadcaster robot. 
* Run Listener.js on listener robots 
   * There can be multiple listener robots (we had 4). To ensure that all listener messages receive the IR message at the same time, the distance between each broadcaster + listener pair should roughly the same across listener robots.  
* To set the paths for each robot, change the points array as desired