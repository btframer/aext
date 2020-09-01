
------------------------------------------
This is prepare to executing and installing test scripts

If python is installed and you don't want a version conflict, you can run it through a virtual environment.

1. Install Python3  from https://www.python.org/

2. Install virtualenv
> [PATH_TO_PYTHON_DIR]\Scripts\pip install virtualenv
> [PATH_TO_PYTHON_DIR]\Scripts\virtualenv ENV

3. Activate virtual environment
> ENV\Scripts\activate.bat

4. Install serial port and cobs lib
> pip install pyserial
> pip install cobs

5. Run scripts
> python script_name.py COM3


------------------------------------------
Type of scripts 
serialport_test.py - Serial port loopback test. Data send to serial port and wait for recevied. 
                      After recived data will compare. This script can be used to check serial port and device connected to serial port.

read_register.py - Read register.  

write_register.py - Write register.  


                   







