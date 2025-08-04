import re

def is_valid_ip(ip):
    pattern = re.compile(r'^(\d{1,3}\.){3}\d{1,3}$')
    if pattern.match(ip):
        parts = ip.split('.')
        for part in parts:
            if int(part) < 0 or int(part) > 255:
                return False
            return True
        return False
    

def main():
    while True:
        ip = input("Enter IP address: ").strip()
        if ip.lower() == 'q':
            print("Exiting...")
            break
        if is_valid_ip(ip):
            print(f"{ip} is valid IP address")
        else:
            print(f"{ip} is invalid IP address")

if __name__ == "__main__":
    main()