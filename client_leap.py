#!/usr/bin/env python3
"""
UDP Client for Leap Year Checker
Design of Telematic Systems, UC3M

This client program sends a year to the server and receives whether it's a leap year.
Authors:
	Lucas Kohley Aguilar - 100497018
	Laura Pons García - 100496761
"""

import socket

def main():
    # Client configuration
    HOST = 'localhost'
    PORT = 12345
    BUZZER_SIZE = 1024

    
    # Create UDP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print("Leap Year Checker Client")
    print("Enter 'exit' to quit")
    
    while True:
        # Get input from user
        year = input("\nEnter a year to check: ")
        
        try:
            # Send data to server
            client_socket.sendto(year.encode(), (HOST, PORT))
            
            # Check if user wants to exit
            if year.lower() == 'exit':
                print("Closing connection...")
                break
            
            # Receive response from server
            data, _ = client_socket.recvfrom(BUZZER_SIZE)
            response = data.decode()
            
            # Print server's response
            print(response)
            
        except Exception as e:
            print(f"Error: {e}")
            break
    
    # Close socket
    client_socket.close()
    print("Client shutdown complete.")

if __name__ == "__main__":
    main()
