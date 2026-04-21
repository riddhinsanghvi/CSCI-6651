def is_valid_packet(packet):
    """
    Check if packet matches the valid format:
    STX + 4 integer digits + '.' + 3 decimal digits + CR + LF
    """
    if len(packet) < 9:
        print("len(packet) < 9 = False")
        return False
    
    # Check start and end markers
    if not packet[0].isdigit():
        print(" not packet[0].isdigit() = False")
        return False
    if not packet.endswith("\r\n"):
        print("not packet.endswith(rn) = False")
        return False
    
    # Ensure there's exactly one decimal point
    if packet.count('.') != 1:
        print("packet.count('.') != 1 False")
        return False

    # Extract numeric part
    numeric_part = packet[:-2]  # remove \r\n
    try:
        float(numeric_part)
        return True
    except ValueError:
        return False


def decode_packet(packet):
    """Convert valid packet string into a float value."""
    try:
        numeric_part = packet[:-2]  # remove CRLF
        return float(numeric_part)
    except Exception:
        return None


def main():
    input_filename = "packets.txt"  # input file name
    output_filename = "decoded.txt" # output file name

    with open(input_filename, "r") as infile:
        print("File opened")
        data = infile.read()
    
    print(data)
    data = data.replace("\\r\\n", "\r\n")

    # Split packets by CRLF sequence
    # Since each packet ends with \r\n, split using it
    raw_packets = [p + "\r\n" for p in data.split("\r\n") if p]

    print(raw_packets)
    valid_count = 0
    results = []

    for i, packet in enumerate(raw_packets, start=1):
        if is_valid_packet(packet):
            decoded_value = decode_packet(packet)
            print(f"Decoded Value: {decoded_value}")
            results.append(f"Packet {i}: {decoded_value}")
            valid_count += 1
        else:
            results.append(f"Packet {i}: INVALID")

    results.append(f"\nTotal valid packets: {valid_count}")
    results.append(f"Total invalid packets: {len(raw_packets) - valid_count}")

    with open(output_filename, "w") as outfile:
        outfile.write("\n".join(results))

    print("Decoding complete.")
    print(f"Valid packets: {valid_count}")
    print(f"Invalid packets: {len(raw_packets) - valid_count}")
    print(f"Results saved to {output_filename}")


if __name__ == "__main__":
    main()
