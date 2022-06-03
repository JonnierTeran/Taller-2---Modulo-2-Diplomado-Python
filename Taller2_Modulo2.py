# -*- coding: utf-8 -*-
"""
Created on Tue May 

@author: jonnier andres teran
"""

# Taller N1 - Modulo 2   "LOS DATOS Y YO"
# Autor: Jonnier Andres Teran Morales
# Correo= Jonnier.teran@upb.edu.co
# ID No. 502195
# id: 1003064599
# Cel: 3245644212

import pandas as pd

#1. Lea la base de datos netflix_titles usando la librería “pandas”.
Data_F = pd.read_csv('netflix_titles.csv')

#2. Imprima por consola las primeras y últimas 5 filas del arreglo. 
print(Data_F.head(5))
print(Data_F.tail(5))

#3. Imprima cada uno de los tipos de dato asociado a las etiquetas.
Types= Data_F.dtypes
print(Types)

# 4. Guarde un archivo .xlsx, en el cual el nombre del archivo sea “Netflix_list” y el nombre de la
# hoja sea “títulos”.
Data_F.to_excel("Netflix_list.xlsx", sheet_name="titulos", index = False)

#5. Cree una nueva data frame en el cual segmente únicamente: el tipo, la duración, la
# descripción y el país.

New_Data_F = Data_F[["type", "duration", "description", "country"]]

#6. Haga un filtro para las películas que tienen una duración superior a 100 min.
Mov = New_Data_F[New_Data_F["type"] == "Movie"]
Duration = Mov["duration"].str.split(expand=True).dropna()
Mov.insert(4,"durationIntMovies", Duration[0].astype(int))
Movies_Max100 = Mov[Mov["durationIntMovies"] > 100]
print(Movies_Max100) 


#7 Haga un filtro para los "Tv shows" que tienen mas de 3 temporadas 
series = Data_F[Data_F["type"] == "TV Show"]
Duration = series["duration"].str.split(expand=True).dropna()
series.insert(5, "durationIntSeries", Duration[0].astype(int))
FiltBy3 = series[series["durationIntSeries"] > 3]
print(FiltBy3)

# 8. Haga un filtro en el cual solo tenga en cuenta 2 categorías/etiquetas (libre elección).
New_Categories = (Data_F[["director", "country"]])

#9 Recuerde usar casos con indexacion numerica y con texto (loc/ iloc)
Data_F_Country=  Data_F.loc[:1, "country"] = 'non'
Data_F_Country2= Data_F.iloc[:2, 6] = 'none'

#10 Modifique los valores del ID de las 5 primeras y 5 ultimas "shows"
Data_F["show_id"] = Data_F["show_id"].replace({"s1":"1","s2":"2","s3":"3","s4":"4","s5":"5"})
Data_F["show_id"] = Data_F["show_id"].replace({"s8803":"8803","s8804":"8804","s8805":"8805","s8806":"8806","s8807":"8807"})
print (Data_F)
