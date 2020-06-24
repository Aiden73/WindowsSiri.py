decision_to_turn_km_to_miles_or_miles = input("What d you want to convert\nkm to miles or miles to km\nfeet to metres or metres to feet\ninches to centimetres\ncentimtres to feet")

if decision_to_turn_km_to_miles_or_miles.lower == "km to miles":
    km = input("How many kms do you want to want to conbert to miles?\n")
    km_converted_to_int = int(km)
    km_converted_result = km_converted_to_int*0.62137
    print(km_converted_result)

elif decision_to_turn_km_to_miles_or_miles == "miles to km":
    miles = input("How many kms do you want to want to conbert to miles?\n")
    miles_converted_to_int = int(miles)
    miles_converted_result =miles_converted_to_int/0.62137
    print(miles_converted_result)

elif decision_to_turn_km_to_miles_or_miles.lower == "feet to metres":
    feet = input("How many feet do you want to want to conbert to metres?\n")
    feet_converted_to_int = int(feet)
    feet_converted_result = feet_converted_to_int/3.281
    print(feet_converted_result)

elif decision_to_turn_km_to_miles_or_miles == "miles to km":
    metres = input("How many kms do you want to want to conbert to miles?\n")
    metres_converted_to_int = int(metres)
    metres_converted_result =metres_converted_to_int/0.62137
    print(metres_converted_result)

elif decision_to_turn_km_to_miles_or_miles.lower == "feet to metres":
    feet = input("How many feet do you want to want to conbert to metres?\n")
    feet_converted_to_int = int(feet)
    feet_converted_result = feet_converted_to_int/3.281
    print(feet_converted_result)

elif decision_to_turn_km_to_miles_or_miles == "miles to km":
    metres = input("How many kms do you want to want to conbert to miles?\n")
    metres_converted_to_int = int(metres)
    metres_converted_result =metres_converted_to_int/0.62137
    print(miles_converted_result)  


