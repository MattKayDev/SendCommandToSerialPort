import serial
import time

def main():
    # Configure the serial port
    ser = serial.Serial(
        port='COM14',       # Replace with current COM port
        baudrate=9600,      # Set baudrate
        timeout=1           # Timeout for reading
    )
    
    try:
        # Open the serial port if it's not already open
        if not ser.is_open:
            ser.open()
        
        i = 1 # Temp data
        last_id = "" # Temp data

        while i == 1:#temp loop
            # Send a command to the serial device
            command = '050020\r\n'  # Replace with commandto scan
            ser.write(command.encode())
            
            # Allow some time for the device to respond
            time.sleep(1)
            
            # Read the response from the device
            response = ser.read_all().decode('utf-8')
            # Check if the response isn't "0000\r"
            if response != '0000\r':
                #Check if the response isnt last id
                if last_id != response:
                    # Print the response
                    print(response)
                    # Set response to last id
                    last_id = response

    except serial.SerialException as e:
        print(f"Serial error: {e}")
    finally:
        # Close the serial port
        ser.close()

if __name__ == "__main__":
    main()