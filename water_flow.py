def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    # Given density of water in kg/m^3
    water_density = 998.2
    
    # Calculate pressure loss using the given formula
    pressure_loss = (-0.04 * water_density * (fluid_velocity ** 2) * quantity_fittings) / 2000
    
    return pressure_loss  # The result is in kilopascals (kPa) 

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculates and returns the Reynolds number for a pipe with water flowing through it.

    Args:
        hydraulic_diameter (float): The hydraulic diameter of the pipe in meters.
        fluid_velocity (float): The velocity of the water flowing through the pipe in meters/second.

    Returns:
        float: The Reynolds number.
    """

    density = 998.2  # kg/m^3
    dynamic_viscosity = 0.0010016  # Pa*s

    reynolds = (density * hydraulic_diameter * fluid_velocity) / dynamic_viscosity
    return reynolds

# Example usage 
if __name__ == "__main__":
    diameter = 0.1  # meters
    velocity = 2.0  # meters/second

    re = reynolds_number(diameter, velocity)
    print(f"Reynolds number: {re}")


def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculates the water pressure lost because of water moving from a pipe with a large diameter 
    into a pipe with a smaller diameter.
    Returns:
        float: The lost pressure in kilopascals.
    """

    density = 998.2  # kg/m^3

    k = (0.1 + (50 / reynolds_number)) * (((larger_diameter / smaller_diameter)**4) - 1)
    pressure_loss = -k * density * (fluid_velocity**2) / 2000

    return pressure_loss

# Example usage 
if __name__ == "__main__":
    larger_diameter = 0.1  # meters
    fluid_velocity = 2.0  # meters/second
    reynolds_number = 100000  # Example Reynolds number
    smaller_diameter = 0.05  # meters

    pressure_loss = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter)
    print(f"Pressure loss: {pressure_loss} kPa")

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
if __name__ == "__main__":
    main()
