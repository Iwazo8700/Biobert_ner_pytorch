import pandas as pd


diretorios = ['AnatEM-IOB', 'NCBI-disease-IOB', 'BC2GM-IOB', 'BC4CHEMD', 'BC5CDR-IOB', 'BioNLP09-IOB', 'BioNLP11EPI-IOB', 'BioNLP11ID-IOB', 'BioNLP13CG-IOB', 'BioNLP13GE-IOB', 'BioNLP13PC-IOB', 'CRAFT-IOB']
diretorios = ["AnatEM-IOB", 'NCBI-disease-IOB', 'CRAFT-IOB', 'BC2GM-IOB',
        'BC4CHEMD', 'BC5CDR-IOB']
train = pd.DataFrame({'word': [], 'label': []})
test = pd.DataFrame({'word': [], 'label': []})
devel = pd.DataFrame({'word': [], 'label': []})

train = train.reindex(columns=['word', 'label'])
test = test.reindex(columns=['word', 'label'])
devel = devel.reindex(columns=['word', 'label'])


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

print(train.head())
for diretorio in diretorios:
	local_train = pd.read_csv(diretorio+'/train.tsv', delimiter='\t', names=['word', 'label'], quoting=3, error_bad_lines=False)
	local_test = pd.read_csv(diretorio+'/test.tsv', delimiter='\t', names=['word', 'label'], quoting=3, error_bad_lines=False)
	local_devel = pd.read_csv(diretorio+'/devel.tsv', delimiter='\t', names=['word', 'label'], quoting=3, error_bad_lines=False)
	
	#print(diretorio, ':', sorted(list(set(df['label'].values))))

	train = train.append(local_train, ignore_index=True, sort=False)
	test = test.append(local_test, ignore_index=True, sort=False)
	devel = devel.append(local_devel, ignore_index=True, sort=False)

print(train.head())
#print(sorted(list(set(train['label'].values))))
train = train.dropna()
test = test.dropna()
devel = devel.dropna()
for tag in Tags:
	for string in tag:
		train = train.replace(regex = r'{}'.format(string), value = tag[0])	
		test = test.replace(regex = r'{}'.format(string), value = tag[0])
		devel = devel.replace(regex = r'{}'.format(string), value = tag[0])


print(sorted(list(set(train['label'].values))))
print(train.head())

train.to_csv('train.tsv', sep='\t', index=False, header=False)
test.to_csv('test.tsv', sep='\t', index=False, header=False)
devel.to_csv('devel.tsv', sep='\t', index=False, header=False)
#print(df.loc[df['label'] == 'B-Taxon'])


