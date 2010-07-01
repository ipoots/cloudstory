from cloudstory.nirvanix import Nirvanix

DRIVERS = {'nirvanix':Nirvanix}
class DriverException(Exception):
    def __init__(self,message):
        self.message = message
    def __str__(self):
        return repr("CloudStory does not have a driver for %s" % (self.message)) 
def get_driver(driver):
    if DRIVERS.has_key(str(driver).lower()):
        return DRIVERS.get(str(driver).lower())
    else:
        raise DriverException(str(driver).lower())
    