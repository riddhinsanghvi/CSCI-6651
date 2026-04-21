class Packet:
    """ Reprents a single packet and checks for validation and also logic for decoding the packet """

    def __init__(self, raw_packet):
        self.raw = raw_packet

    def is_valid_packet(self)->bool:
        """
        Check if packet matches the valid format:
        STX + 4 integer digits + '.' + 3 decimal digits + CR + LF
        """
        #Length check 
        if len(self.raw) < 9:
            print("len(packet) < 9 = False")
            return False
        
        #Check if the first character is a didgit
        if not self.raw[0].isdigit():
            print(" not packet[0].isdigit() = False")
            return False
        
        # Check start and end markers
        if not self.raw.endswith("\r\n"):
            print("not packet.endswith(rn) = False")
            return False
        
        # Ensure there's exactly one decimal point
        if self.raw.count('.') != 1:
            print("packet.count('.') != 1 False")
            return False
        
    def decode_packet(self):
        """Convert valid packet string into a float value."""
        try:
            numeric_part = self.raw[:-2]  # remove CRLF
            return float(numeric_part)
        except Exception:
            return None
        

class PacketFileProcess:
    #this class handles the file processing part i.e., Reading the file, writing in a new file, validating the file, decoding the packets

    def __init__(self, input_file_path:str, output_file_path:str):
        self.input_file_path = input_file_path
        self.outpit_file_path = output_file_path

    def load_packet_file(self):
        """ Read the packet from the file, normalize CLRF characters, create Packet class object  """

        with open(self.input_file_path, "r") as infile:
            print("File opened")
            data = infile.read()
    
        print(data)
        #coneverting the literal escaped CLRF characters to the normal CLRF characters
        data = data.replace("\\r\\n", "\r\n")

        # Split packets by CRLF sequence
        raw_packets = [p + "\r\n" for p in data.split("\r\n") if p]
        print(raw_packets)

        return [Packet (p)for p in raw_packets]
    
    def process(self):
        """ Validate and decode all the packets"""
        packets = self.load_packet_file()

        valid_count = 0
        results = []

        for i, packet in enumerate(packets, start=1):
            if packet.is_valid_packet():
                decoded_value = packet.decode_packet()
                print(f"Decoded Value: {decoded_value}")
                results.append(f"Packet {i}: {decoded_value}")
                valid_count += 1
            else:
                results.append(f"Packet {i}: INVALID")

        results.append(f"\nTotal valid packets: {valid_count}")
        results.append(f"Total invalid packets: {len(packets) - valid_count}")

        print(f"Valid packets: {valid_count}")
        print(f"Invalid packets: {len(packets) - valid_count}")

        self.write_results_in_file(results)
       

    def write_results_in_file(self, results):
         """ Write the results in the output file"""
         with open(self.outpit_file_path, "w") as outfile:
            outfile.write("\n".join(results))

def main():
    """Starting point of the code"""
    input_file_path = "packets.txt"  # input file name
    output_file_path = "decoded.txt" # output file name

    processor = PacketFileProcess(input_file_path, output_file_path)
    processor.process()
    print("Decoding complete.")
    #print(f"Valid packets: {valid_count}")
   # print(f"Invalid packets: {len(packets) - valid_count}")
    print(f"Results saved to {output_file_path}")


if __name__== "__main__":
    main()