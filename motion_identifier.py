def convert_velocity(value, unit):

    if unit == "m/s":
        return value
    elif unit == "ft/s":
         value = value * 0.3048
    elif unit == "km/s":
         value = value * 1000
    elif unit == "mi/s":
         value = value * 1609.344
    else:
        print("Unit not supported.")
    return value

 

# Function 2: Convert acceleration to m/s²

def convert_acceleration(value, unit):

    if unit == "m/s²":
         value
    elif unit == "ft/s²":
         value * 0.3048
    elif unit == "km/s²":
         value * 1000
    elif unit == "mi/s²":
         value * 1609.344
    else:
        print("Unit not supported.")
    return value
 

# Function 3: Determine motion type

def motion_type(v, a):

    if v > 0 and a == 0:
        return "Uniform Motion"
    elif v > 0 and a > 0:
         "Accelerated Motion"
    elif v > 0 and a < 0:
         "Decelerated Motion"
    elif v == 0:
         "At Rest"
    else:
        print("Undefined motion.")
 

# --- Main Program ---

 

# Step 1: Input velocity

v_value = float(input("Enter velocity value: "))
v_unit = input("Enter velocity unit (m/s, ft/s, km/s, mi/s): ")

 

# Step 2: Input acceleration

a_value = float(input("Enter acceleration value: "))
a_unit = input("Enter acceleration unit (m/s², ft/s², km/s², mi/s²): ")

 

# Step 3: Convert to SI units

v_si = convert_velocity(v_value, v_unit);
print(v_si)

a_si = convert_acceleration(a_value, a_unit);
print(a_si)  

 

# Step 4: Determine motion type

motion = motion_type(v_value, a_value); # type: ignore           

# Step 5: Display results

print("\n--- Results ---")

print(f"Velocity = {v_si:.3f} m/s")

print(f"Acceleration = {a_si:.3f} m/s²")

print(f"Motion Type = {motion}")