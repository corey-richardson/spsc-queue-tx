# SPSC Queue Transmitter

## Single-Producer Single-Consumer Serial Hosts

- [spsc-queue](https://github.com/corey-richardson/spsc-queue) (C++)
- [spsc-queue-rs](https://github.com/corey-richardson/spsc-queue-rs) (Rust)

## Packet Protocol

Each packet is 6 bytes in big-endian byte order.

| Offset  | Field          | Type             | Description                                               |
| ------- | -------------- | ---------------- | --------------------------------------------------------- |
| `0`     | Sync Byte      | `u8`             | Frame sync indicator `0x55`                               |
| `1..=2` | Sensor Value 1 | `i16` big-endian | First signed sensor reading                               |
| `3..=4` | Sensor Value 2 | `i16` big-endian | Second signed sensor reading                              |
| `5`     | Checksum       | `u8`             | Bitwise NOT of the low 8 bits of the sum of bytes `0..=4` |

## BBC micro:bit V2 Transmitter

- [spsc-queue-tx/bbc-microbit-v2](/bbc-microbit-v2/)

MicroPython transmitter firmware for the BBC micro:bit V2 that streams sensor data over USB serial in 6-byte binary frames.

Baud rate set to `115_200`.

The micro:bit V2 has no built-in gyroscope; the default loop reads `accelerometer.get_x()` and `accelerometer.get_y()`.

`struct` and `microbit` are built into MicroPython on the device. No external dependencies are required.
