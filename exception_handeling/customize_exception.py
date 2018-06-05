# Author: Real   
# CreateTime 6/1/2018-9:17 AM   
# IDE: PyCharm


class CustomizeException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


try:

    raise CustomizeException('This is my customize exception')

except CustomizeException as ce:
    print(ce)
