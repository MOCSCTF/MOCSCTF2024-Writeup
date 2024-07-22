def modify_exe(input_file, output_file):
    with open(input_file, 'rb') as f:
        content = bytearray(f.read())
    for i in range(len(content)):
        if content[i] != 0x3b and content[i] != 0x00:
            content[i] ^= 0x3b
    with open(output_file, 'wb') as f:
        f.write(content)
if __name__ == "__main__":
    input_file = "MAIN.exe"
    output_file = "output.exe"
    modify_exe(input_file, output_file)
    print("Modification complete.")