from dataset import df1, df2



def execute():
    index1 = df1.set_index('col0 col1'.split()).index
    df2_indexed = df2.set_index('col0 col1'.split())
    index2 = df2_indexed.index
    overlap = index1.intersection(index2)

    df2_indexed.loc[overlap, 'col9'] = 'zzz'
