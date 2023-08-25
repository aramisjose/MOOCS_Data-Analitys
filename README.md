# README

Unos de los principales cometidos de este proyecto era evaluar que tanto influian en el nivel de ventas las variables según idioma, nivel y rating.



EDX

En este apartado estaremos dando un breve contexto de las metricas interesantes que encontramos dentro del dataset de EDX

![nubEdx](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/5d487792-98bf-4fed-858d-39c832c994cd)


En esta instancia tenemos en porcentaje de suscritores por tipo de curso podemos apreciar que en top 5 los cursos con mayor demanda son comunicación, arquitectura, computación, analisis de datos más estadisticas y humanidades. Evaluaremos más de cerca las metricas en el dataset para dar una conclusión  de porque existen más suscriptores en estos tipos de cursos.

![TortaGGtipoCurso](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/f2a1cc8d-b4ed-40ae-aef0-09b8e75836e1)

Segmentación del nivel de ventas respecto a los tipos de nivel en los cursos. 

![VentasXnivelCurso](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/6d14f324-8682-46b7-b4e5-4db61a3c4d2a)


Podemos apreciar en el grafico anterior que existe una mayor demanda en el numero de suscritores en los cursos con un nivel introductorio, se podria decir que a medida que aumentan los niveles en los cursos el nivel de suscriptores baja se debe quizas a:

1_ La mayoria de los suscriptores optan por un curso que lo instruya desde los primeros pasos.

2_ Una vez terminado el nivel introductorio de un curso gran parte de los suscriptores sienten que pueden seguir aprendiendo de manera independiente. 

3_ Pueden haber adquirido los cursos de nivel introductorio por tener un precio más económico sabremos de esto en el siguiente grafico.

Precios por nivel:

![PreciosXnivel](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/f2d5ab85-29d4-43c6-b211-d810fe420ef0)

Aquí es importante resaltar que a medida que los cursos suben de nivel los precios tienden a ser más altos.

En el siguiente gráfico podemos vizualizar la frecuencia acumulada de cursos con el mismo precio.

![FrecuenciaPrecios](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/7b95a834-e6ec-4ceb-a185-de0d28755882)

Como son muchas instituciones con cursos en edx haremos un top 10 de las que tiene  más cursos y ver cuales tiene mayor impacto en el número de suscriptores.

Harvard University                       103
Universitat Politècnica de Valencia       47
Massachusetts Institute of Technology     41
Delft University of Technology            30
IBM                                       30
Inter-American Development Bank           29
The University of Queensland              26
The University of Michigan                22
Tecnológico de Monterrey                  21
Columbia University                       20

![top10_instituciones](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/538725c2-58a0-4fc3-a131-6ac6d6761832)


Es de esperar que los cursos impartidos por la universidad de harvard sean los que tengan una mayor demanda de estudiantes mas sin embargo podemos ver como en el puesto dos a pesar en el top 7 de institutos con mas cursos se posiciona en segundo lugar con mayor cantidad de estudiantes y tambien los cursos de columbia university que a pesar de estar en el top 10 se posicisiona en el tercer lugar con mayor cantidad en matricula de estudiantes, analizaremos inmediatamente por separado que tipos de cursada imparten estos institutos y cual es su impacto en el mercado.

Ahora veremos que tipos de cursos tienen mayor demanda en la universidad de queensland.

![queensland](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/9c1fdaa9-5f89-4ee7-ab22-a3deaf90c5ab)

En un top3 de los cursos con mas matricula de estudiantes estan los cursos de Comunicación con un 61.5%, Gestion de negocios con un 10.2% de la matricula y Humanidades con un  8.4% de la matricula. Siendo estos cursos los más atrativos o con mayor cantidad de suscriptores dentro de esta universidad. Coincidiendo as los cursos de Comunicacion con el top general que se hizo en el grafico de porcentaje de alumnos por tipo de curso.

Ahora veremos que tipos de cursos tienen mayor demanda en la universidad de columbia.

![Columbia](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/8bc8ad33-79ac-4fbc-9268-a3874ba1a1ff)

 Uno de los cursos con mayor demanda en la universidad de Queensland son los de computer science, cursos relacionados a estos temas se pueden sugerir al modelo de negocios que se quiera plantear.

Segmentación del nivel de ventas segun los subtitulos

![demandaXsubtitulos](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/dee03493-1de7-4c23-9f4e-e3bea8895884)

La cantidad de suscritores donde el curso solo tiene el subtitulo de Italiano es muy alta a pesar de que solo hay 4 cursos con esta condición a diferencia de que los cursos con el subtitulo Ingles son mas de 700 cursos presentes en el dataset. Se sugiere implementar los cursos con subtitulo italiano y también con subtitulo Español, Frances, Portugues y Aleman.

Demanda de los cursos con dos subtitulos:

![subtitulos2](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/f72decdf-b437-4c92-a3d4-3ec74e8de958)

Demanda de los cursos con tres subtitulos:

![subtitulos3](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/61d520a0-230f-41ef-b03e-9db46906addd)


Viendo los graficos anteriores se puede apreciar que existen una mayor demanda en los cursos en ingles pero en conjunto con otros lenguajes los cuales son los mas destacados en esta data como lo son: Español, Italiano, Aleman, Portugues, Frances y Chino. 

 
UDEMY


![nubeUdemy](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/0daa2b29-73b5-4ad5-a239-4b8881d70541)


Segmentación de los datos de acuerdo a los niveles en los cursos:

![suscriptoresXnivel1](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/0f112555-a30d-4520-aac4-dc3de821e776)


Podemos apreciar de que los cursos todos los niveles y nivel principiantes son los que cuentan con más suscripciones pagadas,

Tambien es importante ver en que niveles hay mas estudiantes inscriptos si el curso es gratis

![suscriptoresXnivel](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/45c0c0e9-3b47-4ea4-b41a-3e6c62fccdc7)

Es logico que haya una mayor demanda en los cursos que son gratuitos no obstante seria genial establecer una estrategia de marketing que logren fidelizar dichos clientes que obtan por estos cursos de nivel gratuito.

Segmentación del nivel de ventas segun el precio del curso:

![preciosXnivel](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/69e0348f-bef1-4d95-bbaf-cabb53319164)

Ignorando el numero de suscriptores que adquieren los cursos gratuitos podemos apreciar que los cursos con un valor de 200 $ siendo el precio más alto tiene una mayor demanda con respecto a los precios más bajos.

![Precios_udemy](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/e7bcc2b4-46ab-4720-a8c6-f58c603935b3)

Con repecto a los dos gráficos anteriores podemos apreciar de que a pesar de que no hay muchos cursos con el precio de 175$ es uno de los que más suscriptores tiene. Ahora bien podriamos preguntarnos que que tipos de curso con este precio son los que tienen mas suscriptores segmentaremos inmediatamente estas metricas.

![torta175](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/04fc2e16-573b-4885-9bf9-e339123a0ba9)

Es impresionante ver que la mayor demanda en los cursos con mas suscriptores en precios de 175$ son los que estan relacionados con la programción web y business Finance, veremos si estas metricas se dan igual para cursos de 200$ y 30$

![torta200](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/a90cc608-af3b-48fc-bc76-0693c1178e0f)

![torta30](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/ed8e0505-415b-462e-9077-ba6bf0c4c3f5)


En un top 3 podemos apreciar que en estos top de precios vemos que los cursos mas comprados son Musica instrumental, desarrollo web y diseño grafico, veremos a continuación que sucede si hacemos una vision general en todos los cursos de cualquier precio.

![tortaGG](https://github.com/aramisjose/MOOCS_Data-Analitys/assets/67377571/feda7ae8-c823-4753-9d09-e53f31338fa7)


En conclusión tenemos como primera recomendación los cursos orientados a la programación y al desarrollo web asi como tambien los cursos de diseño grafico y finanzas son aquellos que deberiamos considerar para el modelo de negocio que se quiera implementar. Ademas es muy importante resaltar que los cursos de la universidad de Queenslands y Columbia suelen ser muy atractivos para los estudiantes. Tambin es importante resaltar como se vio en los datos que a pesar de tener menos cantidad de cursos de un valor más elevado no tiene un gran diferencia con los cursos que son mas baratos al contrario a pesar de ser menos los cursos con valor más alto estos suelen tener una gran demanda de estudiantes y se debe estos estan orientados a enseñar a los estudiantes las habilidades más demandadas en el mercado autual asi como también un curso más caro puede que le ofrezca al estudiante la mejor experiencia de aprendizaje o que dicho curso este mejor elaborado. En otro caso tenemos la implementación de de varios subtitulos por curso ya que al satisfacer la demanda de estudiantes en difentes regiones del mundo se podra ser más competitivo respecto a las diferentes instituciones que hoy por hoy imparten cursos en linea como un modelo de negocio.


Puede acceder al dashboar aqui -->> https://aramisjose-pi03-data-analitys-ded-yu0gje.streamlit.app/  









