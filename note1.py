import os 
import csv

directory = r'F:\Gatech\8803\project\data'
file = os.path.join(directory,'chinese_tbcov.tsv')      
writefile = open('tweetsid.txt','w+')


def extractid(directory,filename):
    """
    obtain
    """

twidfile = []        
with open(file,encoding="utf8") as fd:
    rd = csv.reader(fd, delimiter="\t", quotechar='"')
    i=0
    for row in rd:
        if i>100:
            break
        else:
            if row[0].isdigit():
                writefile.write(row[0]+'\n')
            i += 1
writefile.close()        