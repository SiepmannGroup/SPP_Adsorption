def makegrid():
    numBins = tuple([600, 600, 1])
    abc = tuple([60.066, 59.697, 13.383]) # unit cell dimensions
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
    xyz('/home/siepmann/josep180/Work/OFS/SPP/SPPgridcheck7.xyz',data)


def micropore(coords):
    #print("in micropore", coords)
    x, y, z = coords
    if ((y < 34.8 and y > 15) or (x > 20.0 and x < 40.0)):
        #print('Located in micropore')
        return True
    else:
        return False

def mesopore(coords):
    #print("in micropore", coords)
    x, y, z = coords
    if (y > 40.8 or y < 9) and (x >46.0 or x < 14.0):
        #print('Located in mesopore')
        return True
    else:
        return False

def surface(coords):
    #print("in micropore", coords)
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
