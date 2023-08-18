# Dom, Nihal and Weronika
# import module sys
import sys
# import module traceback
import traceback

# try to open a file named 'foo'
try:
    f = None  # declare the variable f first
    f = open("foo")
    # f = open("../country.txt")
# catch an exception in case the try block fails
# specifically - no file found
except FileNotFoundError as err:
    # output to the console details of the exception
    print("Could not open",
          # accessing attribute .filename
          "err.filename:", err.filename,  # foo
          # accessing 2nd argument
          "err.args[1]:", err.args[1],
          "file=sys.stderr:", file=sys.stderr)  # No such file or directory
    # print exception arguments
    print("Exception arguments:", err.args, file=sys.stderr)
    # unpack the exception information
    error_type, value, trace_back = sys.exc_info()
    print(f'Error Type {error_type}')
    print(f'Value {value}')
    print(f'Trace Back {trace_back}')
    print(f'Line Number {trace_back.tb_lineno}')
    # traceback.print_exc()  # this is the Traceback error that will be shown as a classic scary error in the console

# start a final block - part of the exception handling
finally:
    # output the given string to the console
    print("Finally block always runs")
    # if our file exists
    if f is not None:
        # close it.
        f.close()
