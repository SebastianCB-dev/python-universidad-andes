import pandas as pd

def calcular_estadisticas(descargas:pd.DataFrame)->pd.DataFrame:

    descargas = descargas.set_index("PAGO")
    descargas = descargas.drop(0, axis=0, errors='ignore')
    descargas = descargas.reset_index()
    stats = descargas.groupby(["MODELO"])[["PAGO"]].describe()
    stats = stats.reset_index()
    stats = stats.sort_values(by=["MODELO"])
    statsE = descargas.groupby(["MODELO"])[["ESTRELLAS"]].describe()
    statsE = statsE.reset_index()
    statsE = statsE.sort_values(by=["MODELO"])
    
    df = pd.DataFrame(columns=['MODELO','CANTIDAD','PROMEDIO','MAXIMO','MINIMO','ESTRELLAS','DESV. ESTRELLAS','COMENTARIO'],index=range(len(stats)))
    
    for j in range(len(stats)):
        t1 = stats.iloc[j,:]
        t2 = statsE.iloc[j,:]
        t3 = descargas[descargas["MODELO"] == t1[0]]
        tc = len(t3[t3['COMENTARIO'] == 'TRUE'])
        
        df.loc[j] = pd.Series({'MODELO':t1[0],'CANTIDAD':t1[1],'PROMEDIO':t1[2],'MAXIMO':t1[8],'MINIMO':t1[4],'ESTRELLAS':t2[2],'DESV. ESTRELLAS':t2[3],'COMENTARIO':tc})
    
    df = df.fillna(0)
    df = df.set_index("MODELO")
    df = df.round(decimals=2)
    
    return df

