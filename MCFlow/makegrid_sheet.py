def makegrid():
    numBins = tuple([1, 500, 1])
    abc = tuple([40.106, 100.0, 40.145]) # unit cell dimensions
    labels = np.chararray(shape=numBins, unicode=True, itemsize=5)
    data = {'atoms':[], 'coords':[]}
    print('bin size = ', [abc[0]/numBins[0], abc[1]/numBins[1], abc[2]/numBins[2]])
    for i in range(numBins[0]):
        for j in range(numBins[1]):
            for k in range(numBins[2]):
                coords = [i*abc[0]/numBins[0], j*abc[1]/numBins[1], k*abc[2]/numBins[2]]
                if micropore(coords):
                    data['atoms'].append( 'D' )
                elif mesopore(coords):
                    data['atoms'].append( 'F' )
                elif surface(coords):
                    data['atoms'].append( 'H' )
                data['coords'].append( coords ) 
    xyz('/home/siepmann/josep180/Work/BTX/MFI-nanogrid.xyz',data)
    
def micropore(coords):
    #print("in micropore", coords)
    x, y, z = coords
    if ((y > 7.4 and y < 52.2) ):
        #print('Located in micropore')
        return True
    else:
        return False

def mesopore(coords):
    #print("in mesopore", coords)
    x, y, z = coords
    if ((y > 99.4 or y > 60.2) ):
        #print('Located in mesopore')
        return True
    else:
        return False

def surface(coords):
    #print("in surface", coords)
    x, y, z = coords
    if not micropore(coords) and not mesopore(coords):
        #print('Located on surface')
        return True
    else:
        return False

from MCFlow.runAnalyzer import what2Analyze
from MCFlow.file_formatting.reader import Movie
from MCFlow.file_formatting.writer import xyz
from MCFlow.analysis_parsers import Results
#from MCFlow.getData import outputDB
from MCFlow.calc_tools import calculate_distance2
import MCFlow.file_organization as fo
import numpy as np

if __name__ == '__main__':
    makegrid()
