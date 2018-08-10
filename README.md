# Clicker-Game-Solver-Bot
A bot designed to automate and solve the act of playing repetitive clicker games after initial setup.

# Setup

Right now it is a Simple experiemental API.

To set up the clicker solver import it into a project you want to use it in, and create a ClickerSolver object. Right now it is set up to run basic commands to immediately set up the mouse control.

# Commands:

object.easySetClickLocations()

-Press A to add a location
-Press W to increase time interval it waits before clicking that location
-Press S to decrease time interval it waits before clicking that location
-Press Q to exit setup and continue


object.easyStart()

-Loops through and clicks on locations that are set up.


object.timedStart()

-Loops through and clicks on locations that are set up with proper timings

WARNING: Experimental feature.



