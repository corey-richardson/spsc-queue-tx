from microbit import accelerometer


def read_accel_xy() -> tuple[int, int]:
    # Accelerometer readings in milli-g
    return accelerometer.get_x(), accelerometer.get_y()
