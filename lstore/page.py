# these are constants but they can be put into config.py
VALUE_SIZE = 8 # size of the data
METADATA_COLUMNS = 4 
INDIRECTION_COLUMN = 0 
RID_COLUMN = 1
TIMESTAMP_COLUMN = 2
SCHEMA_ENCODING_COLUMN = 3


class Page:

    def __init__(self):
        self.num_records = 0
        self.size = 4096
        self.write = True
        self.ptr = 0 # points to end of written portion
        self.data = bytearray(self.size)

    # returns remaining capacity of page
    def has_capacity(self):
        return (self.size - self.ptr)

    # returns a relative pointer of where the write is located on the page
    def write(self, value):
        self.data[self.ptr:self.ptr + VALUE_SIZE] = (value).to_bytes(VALUE_SIZE, "big")
        self.num_records += 1
        self.ptr += VALUE_SIZE

# Not done
class Base_Page:
    def __init__(self, columns):
        self.num_records = 0
        self.columns = columns
        self.pages = [Page()*(METADATA_COLUMNS+columns)]

    """
    Data's first couple columns are metadata
    :returns index of where the record is in each page
    """
    def update(self, *data):
        for index in range(0, len(data)):
            self.pages[index].write(data[index])
        self.num_records += 1
        return self.num_records - 1
    
# Not done
class Tail_Page:
    def _init_(self, columns):
        self.num_records = 0
        self.columns = columns
        self.pages = [Page()*(METADATA_COLUMNS+columns)]

    # Doesn't check if there is space in the page, thats the responsibility of calling function
    def append(self, *data):
        for index in range(0, len(data)):
            self.pages[index].write(data[index])
        self.num_records += 1
        return self.num_records - 1 