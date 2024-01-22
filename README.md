# WhatsApp Contact List Automation Tool

## Introduction
This repository contains the source code and executable files for an automation tool designed to streamline messaging via WhatsApp. Developed to cater to both English and Spanish-speaking users, this tool provides a user-friendly interface to send predefined messages to a contact list.

## Features
- **Multilingual Support**: Executables available in both English and Spanish.
- **Contact Management**: Easy management of contact lists through `.csv` files.
- **Automated Messaging**: Send messages automatically to a predefined list of contacts.
- **Custom Authentication**: Includes a module for custom authentication processes.

## Directory Structure
.  
├── core.py # Core logic for the automation process  
├── custom_auth.py # Custom authentication logic  
├── exceptions.py # Custom exception definitions  
├── log.py # Logging functionalities  
├── open_file.py # Utility to open files  
├── pywhatbot.py # Main script for running the bot  
├── requirements.txt # Required libraries and dependencies  
├── test_pywhatbot.py # Test script for the bot  
├── text.py # Text processing utilities  
├── user_interface.py # User interface logic  
├── contacts.txt # Sample contact list  
├── PyWhatKit_DB.txt # Database file for PyWhatKit  
├── test_image.jpg # Test image file  
├── test_license_key.txt # Test file for license key  
├── english_contacts.csv # English contacts list  
├── spanish_contacts.csv # Spanish contacts list  
├── files/  
│ └── send.png # Image file used in UI  
└── english_executable/ # Folder containing English executable and related files  
└── dist/  
├── PyWhatKit_DB.txt  
├── english_contacts.csv  
├── sapBroBot.exe # English executable  
└── test_image.jpg  
└── spanish_executable/ # Folder containing Spanish executable and related files  
└── dist/  
├── PyWhatKit_DB.txt  
├── spanish_contacts.csv  
├── sapBroBot.exe # Spanish executable  
└── test_image.jpg  


## Usage
- Install the required dependencies from `requirements.txt`.
- Run `pywhatbot.py` for the script version or execute `sapBroBot.exe` in the `english_executable/dist/` or `spanish_executable/dist/` directory for the executable version.
- Follow the instructions in the user interface to input your message and select the contact list file.

## Requirements
- Python 3.x
- Dependencies from `requirements.txt`

## Note
This tool is intended for efficient communication and respects the privacy and guidelines of WhatsApp usage. Please use this tool responsibly.
---
Thank you for exploring the WhatsApp Contact List Automation Tool. We hope it streamlines your communication process effectively.
