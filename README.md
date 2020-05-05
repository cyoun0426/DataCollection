#Data Collection#

The `transform.py` file transforms GPX files to PLT files. It follows the format of the trajectories in the GeoLife dataset. However, there are a few errors that still need to be fixed.
1. The current code does not handle the 'trip segments'. It does not connect the time stamp of the first segment to the time stamp of the second. I wasn't quite sure how to do this, so I left things as they are for now.
2. I realize that the GPX files read almost like JSON files (they are nested). The points that the user marked on the map are listed outside of the points that the Lockito app created. I couldn't figure out how to parse this nested structure, so the current code only takes into account app-generated points. For walking, this is not a big issue, but this is significant for when the mode of transportation is driving.
3. Because I ran a single program to generate the times, I based the time of day on the TripID. This is actually very unrealistic, but I couldn't think of a better solution for automating everything unless each trip was manually run. For example, if the TripID is 0, then the trip starts at 8 AM. If the TripID is 1, then the trip starts at 9 AM. If the TripID is 2, the trip starts at 10 AM. This pattern continues.

The `manual.py` file also transforms GPX files to PLT files. However, this program requires the user to input a filename, date, and time. To see this, I recommend running this command:
    cat input.txt | ./manual.py
This code handles trip segments because the user manually inputs the times. It also solves the third problem that I addressed earlier. However, I still could not figure out how to solve the 2nd problem.

The `gpx` directory contains the correctly named files from the Lockito app. I just downloaded the files from the Team Drive and deleted the files that were named incorrectly.

The `plt` directory contains the transformed files from `transform.py`

the `plt_manual` directory contains the transformed files from `manual.py`

To run the code, I recommend deleting the files in the `plt` and `plt_manual` directories (just to see things better). Please run `transform.py` and `manual.py` from outside the other directories!
