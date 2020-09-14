import pandas as pd

diretorios = ['AnatEM-IOB', 'NCBI-disease-IOB', 'BC2GM-IOB', 'BC4CHEMD', 'BC5CDR-IOB', 'BioNLP09-IOB', 'BioNLP11EPI-IOB', 'BioNLP11ID-IOB', 'BioNLP13CG-IOB', 'BioNLP13GE-IOB', 'BioNLP13PC-IOB', 'CRAFT-IOB']

Anatomy = ['Anatomy', 'Anatomical_system', 'Developing_anatomical_structure', 'Immaterial_anatomical_entity']
Gene = ['Gene', 'Regulon-operon', 'Gene_or_gene_product', 'SO', 'GGP', 'GENE']
Chemical = ['Chemical', 'Simple_chemical', 'CHEBI']
Disease = ['Disease']
Protein = ['Protein', 'Amino_acid']
Organism = ['Organism', 'Organism_subdivision', 'Organism_substance']
Cancer = ['Cancer']
Organ = ['Organ']
Cell = ['Cell', 'Cellular_component', 'Complex', 'CL', 'GO']
Tissue = ['Tissue', 'Multi-tissue_structure']
Pathology = ['Pathology', 'Pathological_formation']

Tags = [Anatomy, Gene, Chemical, Disease, Protein, Organism, Cancer, Organ, Cell, Tissue, Pathology]

for diretorio in diretorios:
    df = pd.read_csv(diretorio+'/train.tsv', delimiter='\t', names=['word', 'label'], quoting=3, error_bad_lines=False)
    df = df.dropna()
    
    for tag in Tags:
	    for string in tag:
		    df = df.replace(regex = r'{}'.format(string), value = tag[0])	

    print(diretorio)
    print(sorted(list(set(df['label'].values))))
