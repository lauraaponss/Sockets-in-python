#!/usr/bin/env python3
"""
UDP Server for Leap Year Checker
Design of Telematic Systems, UC3M

This server program receives a year from a client and checks if it's a leap year.
Author:
	Laura Pons García - 100496761
"""

import socket

def _isLeap(year):
    """
    Check if a given year is a leap year.
    
    Args:
        year (int): The year to check
        
    Returns:
        bool: True if leap year, False otherwise
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def main():
    # Server configuration
    HOST = 'localhost'
    PORT = 12345
    BUZZER_SIZE = 1024
    
    # Create UDP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    
    print(f"Server listening on {HOST}:{PORT}")
    
    while True:
        try:
            # Receive data from client
            data, addr = server_socket.recvfrom(BUZZER_SIZE)
            year_str = data.decode().strip()
            
            # Check if client wants to exit
            if year_str.lower() == 'exit':
                print("Client requested shutdown. Closing server...")
                break
            
            print(f"\nReceived request from {addr}")
            print("Checking if year input is valid...")
            
            try:
                # Convert received data to integer
                year = int(year_str)
                
                # Check if year is in valid range
                if not (1 <= year <= 9999):
                    print("Year out of valid range!")
                    response = "Year must be between 1 and 9999"
                else:
                    print("Input is valid. Calculating leap year...")
                    # Check if it's a leap year
                    if _isLeap(year):
                        response = f"The year {year} is a leap year!"
                    else:
                        response = f"The year {year} is not a leap year :("
                    print(f"Result: {response}")
                        
            except ValueError:
                print("Invalid input: not an integer!")
                response = "This is not an integer"
                
            # Send response back to client
            print("Sending response to client...")
            server_socket.sendto(response.encode(), addr)
            
        except Exception as e:
            print(f"Error: {e}")
            continue
    
    # Close socket
    server_socket.close()
    print("Server shutdown complete.")

if __name__ == "__main__":
    main()
