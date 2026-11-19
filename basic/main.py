mission_route = (
    "Earth",
    "Luna Station",
    "Mars",
    "Europa",
    "Titan",
    "Neptune Station"
)

print("Our first destination:", mission_route[0])
print("Last Destination:", mission_route[-1])
print("The total amount of destinations:",len(mission_route))
print("\nThe Mission Route is listed below:")

for destination in mission_route:
    print(destination)

if "Europa" in mission_route:
    print("Europa is included in this current mission route.")
else:
    print("Europa is not included in the mission route")


