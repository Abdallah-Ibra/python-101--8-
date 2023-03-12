
# ! =========================================*#
# * ============= File Handling =============*#
# ! =========================================*#

#? f = open(filename, mode,encoding)

# ** Where the following mode is supported:

#! ==> r: open an existing file for a read operation.
#! ==> r+:  To read and write data into the file. The previous data in the file will not be deleted.

#! ==> w: open an existing file for a write operation. If the file already contains some data then it will be overridden. 
#! ==> a:  open an existing file for append operation. It won’t override existing data.
#! ==> w+: To write and read data. It will override existing data.
#! ==> a+: To append and read data from the file. It won’t override existing data.



##?# File Handling Methods ###

#? ==> open()
#? ==> close()

#! ==> with open() as

### Reading Methods ### 
#* ==> read()  ## <str>
#* ==> readline()
#* ==> readlines() ## <list>
#* ==> readable() ## Boolean Value	

### Writting Methods ###
#* ==> write()
#* ==> writelines()
#* ==> writable() ## Boolean Value


