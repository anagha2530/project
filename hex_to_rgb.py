def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip('#')
    if len(hex_code) != 6:
        raise ValueError("HEX code should be 6 characters long")
    
    r = int(hex_code[0:2], 16)
    g = int(hex_code[2:4], 16)
    b = int(hex_code[4:6], 16)
    return (r, g, b)

def main():
    print("HEX to RGB converter")
    while True:
        hex_code = input("enter the hexcode(or 'q' to exit): ")
        if hex_code.lower() == 'q':
            print('exit')
            break

        try:
            rgb = hex_to_rgb(hex_code)
            print(f"RGB: {rgb}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()