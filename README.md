# Leap Year Checker (UDP Client-Server)

A simple client-server application that checks whether a year is a leap year using UDP protocol. This project was developed as part of the Design of Telematic Systems course at UC3M.

## 📋 Overview

This application consists of two Python scripts:
- **server_leap.py**: A UDP server that listens for year inputs and responds with whether the year is a leap year
- **client_leap.py**: A UDP client that sends user-input years to the server and displays the results

The application demonstrates basic socket programming using UDP (User Datagram Protocol) in Python and implements the leap year checking algorithm.

## 🧮 Leap Year Algorithm

A leap year is determined by the following rules:
- Years divisible by 4 are leap years
- EXCEPT years divisible by 100 are NOT leap years
- UNLESS they are also divisible by 400, in which case they ARE leap years

## 🛠️ Features

- UDP-based client-server communication
- Input validation for years (accepts integers between 1-9999)
- Clean error handling for invalid inputs
- Simple command-line interface
- Option to exit the application gracefully

## 📦 Requirements

- Python 3.x
- Standard library modules (no external dependencies)

## 🚀 How to Run

### Starting the Server

```bash
python server_leap.py
```

The server will start listening on localhost:12345.

### Starting the Client

```bash
python client_leap.py
```

The client will prompt you to enter a year. Type a year and press enter to check if it's a leap year.

Type `exit` to close the connection and shut down the client.

## 📝 Example Usage

```
Leap Year Checker Client
Enter 'exit' to quit

Enter a year to check: 2024
The year 2024 is a leap year!

Enter a year to check: 2100
The year 2100 is not a leap year :(

Enter a year to check: 2000
The year 2000 is a leap year!

Enter a year to check: exit
Closing connection...
Client shutdown complete.
```

## 👥 Author

- Laura Pons García

## 📚 Course Information

Developed for the Design of Telematic Systems course at Universidad Carlos III de Madrid (UC3M).
