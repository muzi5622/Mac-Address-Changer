# MAC Address Changer Program

Welcome to my **MAC Address Changer** program! This repository contains a Python script that I developed while learning ethical hacking and Python programming. The script allows users to change their device's MAC address and verify if the change was successful.  

## 📜 Features

- Retrieve the current MAC address of a specified network interface.  
- Change the MAC address to a user-specified value.  
- Validate whether the MAC address change was successful.  

## 🚀 Getting Started  

### Prerequisites  
- Python 3.x & Python 2 
- Administrative privileges (required to run network-related commands).  

### Installation  

1. Clone the repository:  
   ```bash
   git clone https://github.com/muzi5622/Mac-Address-Changer.git
   cd mac-address-changer
   ```  

2. Ensure the necessary permissions:  
   ```bash
   chmod +x mac_changer.py
   ```  

### Usage  

Run the script with the following arguments:  
- `-i` or `--interface` to specify the network interface.  
- `-m` or `--mac` to specify the new MAC address.  

Example:  
```bash
sudo python3 mac_changer.py -i eth0 -m 00:11:22:33:44:55
```  

### Expected Output  

The script will:  
1. Display the current MAC address.  
2. Change the MAC address to the user-specified value.  
3. Confirm whether the change was successful.  

## 💡 Suggestions or Issues  

If you have any suggestions for improvement, encounter issues, or have questions, feel free to:  
- Open an issue in this repository.  
- Contact me directly.  


This program is created for educational purposes only. Use it responsibly and ensure compliance with all applicable laws and regulations.  
