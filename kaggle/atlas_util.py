
# Utils
from pathlib import Path

def removeBasePathAndConvertToString(basePath: Path, src: Path):
    return str(src).replace(str(basePath),'')

#def test_removeBasePath():
#    ans = removeBasePath(Path('/home/ste/.fastai/data/human-protein-atlas'))(Path('/home/ste/.fastai/data/human-protein-atlas/test/b47007ae-bacb-11e8-b2b8-ac1f6b6435d0_blue.png')
#    assert 'test/b47007ae-bacb-11e8-b2b8-ac1f6b6435d0_blue.png' == ans

# Support function: extract file name
extractFileName = lambda l: l.stem
# test
def test_extractFileName():
    ans = extractFileName(Path('/home/ste/.fastai/data/human-protein-atlas/test/b47007ae-bacb-11e8-b2b8-ac1f6b6435d0_blue.png'))
    assert 'b47007ae-bacb-11e8-b2b8-ac1f6b6435d0_blue' == ans


# Support function: extract protein from file name
extractProtein = lambda l: l.split('_')[0]
# test
def test_extractProtein():
    ans = extractProtein('b47007ae-bacb-11e8-b2b8-ac1f6b6435d0_blue')
    assert 'b47007ae-bacb-11e8-b2b8-ac1f6b6435d0' == ans


# Support function: extract protein from file name
extractFilt = lambda l: l.split('_')[1]

def test_extractFilt():
    assert (extractFilt('b47007ae-bacb-11e8-b2b8-ac1f6b6435d0_blue')) == 'blue'


# Support function: convert classes to array
classesStrToArray = lambda l: l.split(' ') # Warning!! Array of string
# Usage sample
def test_classesStrToArray():
    assert (classesStrToArray('7 1 2 0')) == ['7','1','2','0']


# Flat operator for list:
# Transform List[List[a]] -> List[a]
flat_list = lambda l: [item for sublist in l for item in sublist] # flat operator for list
# Test
def test_flat_list():
    src = [[1,2,3,4],[5,6,7]]
    assert flat_list(src) == [1,2,3,4,5,6,7,]