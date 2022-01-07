'''This programs runs the traceroute command from a bat script and saves the output in a file on my local computer. 
Reference to the idea https://github.com/network-charles/Periodic-Traceroute. Used elif statement isnide the 
for loop instead of repeating if statements.'''

#importing the subprocess module that will allow running the bat script inside this Python script.
import subprocess

#defining a function to run the trace when it is called.
def trace():
    #calling the bat file. This is saved in the same folder as the Python script. If you save it somewhere else, you will need to specify the path.
    subprocess.call(['tracer.bat'])

#Here, we use a for loop to run the trace three times and display an output when each trace has been completed.
for i in range(3):
    if i == 0:
        trace()
        print('First traceroute completed successfully.')
    elif i == 1:
        trace()
        print('Second traceroute completed successfully.')
    elif i == 2:
        trace()
        print('Third traceroute completed successfully.')
    