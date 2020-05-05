#Data Collection#

The `transform.py` file transforms .gpx files to .plt files. It follows the format of the trajectories in the GeoLife dataset. However, there are a few errors that still need to be fixed.
1. The current code does not handle the 'trip segments'. It does not connect the time stamp of the first segment to the time stamp of the second. I wasn't quite sure how to do this, so I left things as they are for now.
2. I realize that the gpx files read almost like json files (they are nested). The points that the user marked on the map are listed outside of the points that the Lockito app created. I couldn't figure out how to parse this nested structure, so the current code only takes into account app-generated points. For walking, this is not a big issue, but this is significant for when the mode of transportation is driving.
3. Because I ran a single program to generate the times, I based the time of day on the TripID. This is actually very unrealistic, but I couldn't think of a better solution for automating everything unless each trip was manually run. For example, if the TripID is 0, then the trip starts at 8 AM. If the TripID is 1, then the trip starts at 9 AM. If the TripID is 2, the trip starts at 10 AM. This pattern continues.

The `gpx` directory contains the correctly named files from the Lockito app. I just downloaded the files from the Team Drive and deleted the files that were named incorrectly.

The `plt` directory contains the transformed files.

To run the code, I recommend deleting the files in the `plt` directory (just to see things better). Please run `transform.py` from outside the other two directories!
