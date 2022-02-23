from dataset import df1, df2


def execute():
    df2subset = df2.merge(df1, on='col0 col1'.split(), how='left')
    df2subset.loc[:, 'col9'] = 'zzz'
