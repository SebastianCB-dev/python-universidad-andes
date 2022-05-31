import pandas as pd
def calcular_estadisticas(descargas: pd.DataFrame) -> pd.DataFrame():

    descargas_filtro_pago = descargas.loc[descargas['PAGO'] > 0]

    descargas_filtro_pago = descargas_filtro_pago.sort_values(
        by='MODELO', ascending=False)

    descargar_por_modelo = descargas_filtro_pago.groupby(by=['MODELO'])

    df_result = descargar_por_modelo[['PAGO', 'ESTRELLAS']].mean()
    df_result['DESV. ESTRELLAS'] = descargar_por_modelo['ESTRELLAS'].std()
    df_result['CANTIDAD'] = descargar_por_modelo['PAGO'].count()
    df_result['MINIMO'] = descargar_por_modelo['PAGO'].min()
    df_result['MAXIMO'] = descargar_por_modelo['PAGO'].max()

    df_result['COMENTARIOS'] = descargar_por_modelo.filter(lambda x: (x['COMENTARIO']==True).all()).sum()['COMENTARIO']

    df_result = df_result.rename(columns={'PAGO': 'PROMEDIO'})
    df_result = df_result[['CANTIDAD', 'PROMEDIO', 'MAXIMO',
                        'MINIMO', 'ESTRELLAS', 'DESV. ESTRELLAS', 'COMENTARIOS']]
    df_result[['DESV. ESTRELLAS']] = df_result[[
        'DESV. ESTRELLAS']].fillna(0)
    df_result[['COMENTARIOS']] = df_result[['COMENTARIOS']].fillna(0)

    df_result[['PROMEDIO', 'ESTRELLAS', 'DESV. ESTRELLAS']] = df_result[[
        'PROMEDIO', 'ESTRELLAS', 'DESV. ESTRELLAS']].round(2)
    return df_result
