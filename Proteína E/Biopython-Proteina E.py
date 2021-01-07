from Bio.SeqUtils import GC
from Bio import Entrez

#Un E-mail de ejemplo
Entrez.email = "A.N.Other@example.com"

#una función que busca con biopython el gen que se le pida de la bas de datos de genes de NCBI
def Gene(gen,organismo):
    handle = Entrez.esearch(db="gene", 
                            term=organismo + "[Orgn] AND " + gen + "[Gene]", 
                            idtype="acc")
    record = Entrez.read(handle)
    
    handle = Entrez.esummary(db="gene", 
                             id=str(record['IdList'][0]))
    record = Entrez.read(handle)

    info = record['DocumentSummarySet']['DocumentSummary'][0]
    
    print('----------------------------')
    print('Gen:',info['Name'])
    print('Nombre:',info['Description'])
    print('Organismo:',info['Organism']['ScientificName'])
    print('Locus:',"Cromosoma {}, {}, {}"
          .format(info['Chromosome'],
                  info['MapLocation'],
                  info['GenomicInfo'][0]['ChrAccVer']))
    print('Exones:',info['GenomicInfo'][0]['ExonCount'])
    print(info['Summary'])
    
    handle.close()

# aquí le damos el id de acceso de la proteina E
Gene('GU280_gp04','SARS-COV2')