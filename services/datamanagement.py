import pandas as pd # importando o pandas
# PANDAS: FORMATO DATAFRAME, LEITURA DO ARQ. CSV. 
spotifyinfo2024_df = pd.read_csv("data/spotify_data.csv", encoding="utf-8", sep=",") # leitura do arquivo

spotifyinfo2024_df[['Artist', 'Song']] = spotifyinfo2024_df['Songs & Artist'].str.extract(r'(.+?) - (.+)')

spotifyinfo2024_df = spotifyinfo2024_df.drop(columns=['Songs & Artist'])

pd.set_option('display.max_rows', None) # TIRA O LIMITE DE LINHAS, MOSTRAR TODAS
pd.set_option('display.max_columns', None) # O MESMO MAS COM COLUNAS

spotifyinfo2024_df.rename(columns={
    "Song": "Música",
    "Artist": "Artista",
    "Streams": "Número de Streams",
    "Daily": "Número de Streams em 24 horas"}, inplace=True) 