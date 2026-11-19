mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

destination = input ("\n Enter a destination you want to search for: ")
if destination in mission_route:
    print(destination, "is currently part of the mission route.")

    position = mission_route.index(destination)
    print("stops from start", position)
    stops_from_end = len(mission_route) -1 - position
    print("Current amount of stops from the  end:", stops_from_end)
    if position < len(mission_route) - 1:
        next_stop = mission_route[position + 1]
        print("The next stop is:", next_stop)
    else:
        print("this is the final stop of the journey. Your mission has come to an end.")

else: print(destination, " is not part of the mission route. Try again.")



