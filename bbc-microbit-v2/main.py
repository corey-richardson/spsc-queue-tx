from microbit import Image, display, sleep, uart
from protocol import build_packet
from sensors import read_accel_xy

BAUD_RATE = 115200  # Match config::BAUD_RATE in Rust / C++
LOOP_DELAY_MS = 20  # ~50 Hz packet rate

uart.init(baudrate=BAUD_RATE, bits=8, parity=None, stop=1)
display.show(Image.YES)
sleep(500)
display.clear()

while True:
    val1, val2 = read_accel_xy()
    uart.write(build_packet(val1, val2))
    sleep(LOOP_DELAY_MS)
    