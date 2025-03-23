import pytest

# if pressure_loss_from_fittings is defined in water_flow.py
from water_flow import pressure_loss_from_fittings

def test_pressure_loss_from_fittings():
    """
    Tests the pressure_loss_from_fittings function using the provided test cases.
    """
    test_cases = [
        (0.00, 3, 0.000, 0.001),
        (1.65, 0, 0.000, 0.001),
        (1.65, 2, -0.109, 0.001),
        (1.75, 2, -0.122, 0.001),
        (1.75, 5, -0.306, 0.001),
    ]

    for velocity, quantity, expected_loss, tolerance in test_cases:
        actual_loss = pressure_loss_from_fittings(velocity, quantity)
        assert abs(actual_loss - expected_loss) <= tolerance, \
            f"Failed for velocity={velocity}, quantity={quantity}. " \
            f"Expected {expected_loss}, got {actual_loss}."

# example usage
if __name__ == "__main__":
    test_pressure_loss_from_fittings()
    print("All tests passed!")

import pytest

# if reynolds_number is defined in water_flow
from water_flow import reynolds_number

def test_reynolds_number():
    """
    Tests the reynolds_number function using the provided test cases.
    """
    test_cases = [
        (0.048692, 0.00, 0, 1),
        (0.048692, 1.65, 80069, 1),
        (0.048692, 1.75, 84922, 1),
        (0.286870, 1.65, 471729, 1),
        (0.286870, 1.75, 500318, 1),
    ]

    for diameter, velocity, expected_reynolds, tolerance in test_cases:
        actual_reynolds = reynolds_number(diameter, velocity)
        assert abs(actual_reynolds - expected_reynolds) <= tolerance, \
            f"Failed for diameter={diameter}, velocity={velocity}. " \
            f"Expected {expected_reynolds}, got {actual_reynolds}."

# Example usage
if __name__ == "__main__":
    test_reynolds_number()
    print("All tests passed!")


from water_flow import pressure_loss_from_pipe_reduction

def test_pressure_loss_from_pipe_reduction():
    """
    Tests the pressure_loss_from_pipe_reduction function using the provided test cases.
    """
    test_cases = [
        (0.28687, 0.00, 1, 0.048692, 0.000, 0.001),
        (0.28687, 1.65, 471729, 0.048692, -163.744, 0.001),
        (0.28687, 1.75, 500318, 0.048692, -184.182, 0.001),
    ]

    for larger_diameter, fluid_velocity, reynolds_number, smaller_diameter, expected_loss, tolerance in test_cases:
        actual_loss = pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter)
        assert abs(actual_loss - expected_loss) <= tolerance, \
            f"Failed for larger_diameter={larger_diameter}, fluid_velocity={fluid_velocity}, " \
            f"reynolds_number={reynolds_number}, smaller_diameter={smaller_diameter}. " \
            f"Expected {expected_loss}, got {actual_loss}."

#test
if __name__ == "__main__":
    test_pressure_loss_from_pipe_reduction()
    print("All tests passed!")