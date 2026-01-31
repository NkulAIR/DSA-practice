import re

def taxi_fare_calculator(passenger_groups):
    # Cost is R20 per person
    fare = [i * 20 for i in passenger_groups]
    return sum(fare)

def academic_record(marks_list):
    # >= 75: Distinction, 50-74: Pass, <50: Fail
    symbols = []
    for i in marks_list:
        if i >= 75:
            symbol = "Distinction"
        if i >= 50 and i <= 74:
            symbol = "Pass"
        if i < 50:
            symbol = "Fail"
        
        symbols.append(symbol)
    
    return symbols

print(academic_record([75, 74, 50, 49])) #["Distinction", "Pass", "Pass", "Fail"]
    

def ussd_menu(correct_option):
    # Simulate a do-while loop for input
    user = input("Enter option: ")
    while user != correct_option:
        print("Invalid selection. Try again.")
        user = input("Enter option: ")
    else:
        print("Bundle Purchased!")



def load_shedding_streak(schedule):
    # Find longest sequence of 1s
    l = 0
    r = 1

    while l <= len(schedule) and r < len(schedule):
        if schedule[l] == 1:
            r += 1
        elif schedule[l] == 1:
            l += 1
        streak = schedule[l:r]
        
        if schedule[l] == 1 and schedule[l+1] == 1:
            r += 1
        else:
            l += 1
    return schedule[l:r].count(1)
                

print(load_shedding_streak([1, 1, 0, 1, 1, 1, 1])) # == 

def pothole_detector(road_depths):
    # Find value > prev and > next
    road_depths = sorted(road_depths)
    biggest = road_depths[1] - road_depths[0]
    for i in range(1, len(road_depths)-1):
        # print(smallest)
        if road_depths[i+1] - road_depths[i] != biggest:
            biggest = road_depths[i+1]
        
    if road_depths.count(biggest) > 1:
        return []
    
    return biggest

print(pothole_detector([10, 5, 5, 10]))

def license_plate_validator(plates):
    # Format: "ABC 123 GP"
    outcomes = {'valid': [], 'invalid': []}
    for plate in plates:
        if number_plate := re.match(r'([A-Z]{3})+(\s)([\w]{3})+(\s)GP', plate):
            outcomes['valid'] = [number_plate.group()]

            # outcomes['invalid'] = plate
    
    return outcomes
        

print(license_plate_validator(["ABC 123 GP", "BadPlate", "XYZ 999 GP"]))
    # return outcomes

# def prepaid_electricity(units, daily_usage):
#     # Subtract usage from units. Check if < 0.
#     pass