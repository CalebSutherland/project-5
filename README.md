#NAME Caleb Sutherland

#EMAIL csutherl@uoregon.edu

#GITHUB https://github.com/CalebSutherland

#DESCRIPTION
Added MongoDB database with buttons to submit and display and tests for them to ACP Brevets Times calculator

- Uses docker compose instead of just docker to build all dependencies and run Flask and MongoDB. After starting with docker compose up, go to localhost:5001 on your browser

- The app takes inputs of either km or miles and converts them, then uses algorithms to calculate start and close times of checkpoints based on start time and brevet distance chosen by the user.
The open time algorithm takes a checkpoint distance and calculates the time by taking the distances of different intervals and their max speed and adding them together. For example, 0-200km mas speed is 34km/h while 200-400km is 32km/h, so to find a checkpoint at 300km, the algorithm adds 200/34 and 100/32 instead of just computing 300/32.

The close time algorithm is similar but it takes into account the fact the times lower than 60 minutes would close before the start closed. The algorithm also uses the official time limits for brevets instead of calculating the final distance close time (for example 200km calculates to 13H20 but the end time for a 200km brevet is 13H30).

- The submit button will insert the data for each checkpoint into a database with MongoDB and the display button will fetch the latest database inserted and display it