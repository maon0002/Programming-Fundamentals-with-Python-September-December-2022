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
