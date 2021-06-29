def calcMissing(readings):
    # Write your code here
    mercurys=[]
    for reading in readings:
        mercury=re.split(r"[\t]",reading)[1]
        try:
            mercury=float(mercury)
        except:
            mercury= None 
        mercurys.append(mercury)
    df=DataFrame(mercurys,columns=['mercury'])
    index_missing=df[df['mercury'].isnull()].index
    df=df.fillna(df.interpolate())
    df.fillna(method='ffill',inplace=True)
    df.fillna(method='bfill',inplace=True)
    processed=df.loc[index_missing]
    print(processed['mercury'].to_string(index=False))
