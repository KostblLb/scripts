#������, ��� ����� �������� � �������� GOLD ����� pandas

import pandas as pd

DIR = 'D:/Dev/sokolov EloE/Data retrieval'

##������ ������ �� ������� �������
dfPivot = pd.read_excel(DIR+'/eloe_antismash_pivot_table_dbg.xlsx')
#����������� ��, ��� ����� ���� ��� ���������
df = pd.DataFrame(dfPivot, columns=['GENBANK', 'PHYLUM',
                                    'CLASS', 'ORDER', 'FAMILY',
                                    'GENUS', 'SPECIES', 'BGC type', 'Indx',
                                    'OXYGEN REQUIREMENT', 'METABOLISM', 'ENERGY SOURCES'#�������������� ����
                                    ])
taxLevel = 'GENUS'#'METABOLISM'#'ENERGY SOURCES'#�������� ��������������� �������. ����������� �� ����
#��������� �� ����
df = df.sort_values(by = taxLevel)
taxa = df[taxLevel].unique().tolist()
#����� ����� ���������� �� ��� ��������� df � ������ taxa