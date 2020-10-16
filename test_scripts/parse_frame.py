import sys
import src.frame as fr

#FILENAME = "input.bin"
FILENAME = ""

if (len(sys.argv) < 2) and len(FILENAME) == 0:
    print ("Required parameters: filename")
    print ("python parse_frame.py input.bin")
    sys.exit(0)

FILENAME = sys.argv[1]

input_frame = fr.Frame()

with open(FILENAME, "rb") as f:
    bytes_read = f.read()
for b in bytes_read:
    if (input_frame.parse_frame(b)):
        print("Frame received:"+str(input_frame))    
        print("value:"+hex(input_frame.get_value()))

