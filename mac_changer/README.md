# MAC Changer Project

## Description

The MAC Changer project is a Python script that allows you to change the MAC address of a network interface on a Unix-like system.

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/mac-changer.git
   cd mac-changer
   ```

2. Run the script with the following command:

   ```bash
   python mac_changer.py -i <interface> -m <new_mac_address>
   ```

   Replace `<interface>` with the name of the network interface you want to modify and `<new_mac_address>` with the desired MAC address.

3. Example:
   ```bash
   python mac_changer.py -i eth0 -m 00:11:22:33:44:55
   ```

## Requirements

- Python 3.x
- Unix-like operating system (e.g., Linux)

## Notes

- Ensure you have the necessary permissions to change the MAC address.
- Use it responsibly and in compliance with applicable laws and regulations.

## Disclaimer

This script is provided as-is without any warranty. Use it at your own risk.

## License

This project is licensed under the [MIT License](LICENSE).
