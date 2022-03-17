from rand_string.rand_string import RandString

from os import mkdir

# functions org

for i in range(4):

    FileBomber = RandString('uppercase',5)

    mkdir(FileBomber)