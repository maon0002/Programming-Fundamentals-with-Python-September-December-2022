# Problem 2 - Destination Mapper
# Problem for exam preparation for the Programming Fundamentals Course @SoftUni.
# Submit your solutions in the SoftUni judge system at https://judge.softuni.org/Contests/Practice/Index/2518#1.
#
# Now that you have planned out your tour, you are ready to go! Your next task is to mark all the points on the map that you are going to visit.
# You will be given a string representing some places on the map. You have to filter only the valid ones. A valid location is:
#     • Surrounded by "=" or "/" on both sides (the first and the last symbols must match)
#     • After the first "=" or "/" there should be only letters (the first must be upper-case, other letters could be upper or lower-case)
#     • The letters must be at least 3
# Example: In the string "=Hawai=/Cyprus/=Invalid/invalid==i5valid=/I5valid/=i=" only the first two locations are valid.
# After you have matched all the valid locations, you have to calculate travel points. They are calculated by summing the lengths of all the valid destinations that you have found on the map.
# In the end, on the first line, print: "Destinations: {destinations joined by ', '}".
# On the second line, print "Travel Points: {travel_points}".
# Input / Constraints
#     • You will receive a string representing the locations on the map
#     • JavaScript: you will receive a single parameter: string
# Output
#     • Print the messages described above
import re


def valid_locations(locations):
    pattern = r'(=|\/)([A-Z][A-Za-z]{2,})\1'
    matches = re.findall(pattern, locations)
    locations_list = []
    for match in matches:
        locations_list.append(match[1])
    calc_points(locations_list)
    return locations_list


def calc_points(valid_locations):
    points = [len(location) for location in valid_locations]
    total_points = sum(points)
    print_result(total_points, valid_locations)
    return total_points


def print_result(total, validated_locations):
    print(f"Destinations: {', '.join(validated_locations)}")
    print(f"Travel Points: {total}")


locations_string = input()
valid_locations(locations_string)
