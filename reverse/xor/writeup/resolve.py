import subprocess

def xor_file_and_extract_strings(filename, output_dir,strings_output_file):
    all_strings = []
    with open(filename, 'rb') as f:
        content = f.read()
    for xor_value in range(1, 256):  # 0x01 to 0xff
        xored_content = bytes([byte ^ xor_value for byte in content])
        output_file = f"output_file_{xor_value:02X}.bin"  # Save with the XOR value in the filename
        with open(output_file, 'wb') as f_out:
            f_out.write(xored_content)

# Example usage:
input_filename = "main.bin"
output_dir = ""
strings_output_file = "all_strings.txt"
xor_file_and_extract_strings(input_filename, output_dir,strings_output_file)