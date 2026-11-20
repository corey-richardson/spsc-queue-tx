import struct

SYNC_BYTE = 0x55


def clamp_i16(value: int) -> int:
    return max(-32768, min(32767, int(value)))


def build_packet(val1: int, val2: int) -> bytes:
    payload = struct.pack(">Bhh", SYNC_BYTE, clamp_i16(val1), clamp_i16(val2))
    checksum = (~(sum(payload) & 0xFF)) & 0xFF
    return payload + bytes([checksum])
