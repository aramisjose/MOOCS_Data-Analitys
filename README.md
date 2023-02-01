# PI03-Data-Analitys

Unos de los pricipeles cometidos de este proyecto era evaluar que tanto influian en el nivel de ventas las variables según idioma, nivel y rating.


Se hizó el análisis exploratorio de datos y también el preprocesamiento y a mi parecer los datasets de Coursera no aportaban mucho al modelo de datos que queria hacer, igualmente limpie los archivos y los normalice para ver si por si acaso los necesitaba más adelante. Los datasets de las plataforma edx y udemy cumplian con el modelo que queria plantear y los limpie elimine duplicados y normalice algunas columnas luego hice un filtro por las columnas que necesitaba y trabaje con la correlación  estadistica para ver como se comportaba el precio con respecto a otras variables.


En la data de Udemy calculé la correlación entre el precio y numero de lecturas y me dio un total de 0.3301604481628124.

Dado que esta correlación es positiva, nos dice que los precios y los números de lecturas están correlacionados positivamente. En otras palabras, a medida que aumentan los valores en la columna de precios, los valores en la columna de número de lecturas tienden a aumentar.

También calcule la correlación entre el precio y el numero de suscriptores y me dio un total de 0.05076934882586656.

Las columnas price y número de suscriptores se correlacionan positivamente. Mientras que más aumentan los precios aumentan el numero de suscriptores, hablando coloquialmente una parte de la población esta dispuesta a pagar más o suscribirse en un curso de buena calidad, como dice el dicho lo barato sale caro, por esto la gente siempre busca la mejor marca o aquel producto que le ofrezca mucho más de lo que le ofrece otros productos. En nuestro analisis no quiere decir que los cursos que valen aproximadamente 25$ sean malos, no!, ya que hay una buena cantidad de personas que han pagado por estos cursos, sin embargo hay una parte de la población que compran y se suscriben a los cursos de mayor valor porque buscan algo más que solo lo basico, por ejemplo los clientes buscan cursos que no solo le den las clases del curso en vivo o grabadas, también buscan variables donde el curso ofrezca certificación o que sean para aprender las habilidades más demandadas en el mercado actual.


En la data de Edx trabaje con la correlación de entre el precio y el numero de estudiantes inscriptos  y la correlación me daba de resultado -0.009482190720812004

Esta correlación es negativa, nos dice que los puntos y las asistencias están correlacionados negativamente. Esto quiere decir que a medida que aumentan los valores en la columna de precios, los valores en la columna de numero de inscristos tienden a disminuir.

![Captura de pantalla (144)](https://user-images.githubusercontent.com/67377571/216084850-b7fe7464-c4d7-4c9e-b6f6-e1fe38b90d18.png)





Viendo este gráfico se podria interpretar que a medida que los cursos aumentan de nivel suelen haber menos estudiantes inscriptos, la razón de esto se debe a que muchos estudiantes no habrán terminado el introductorio, o también que hayan terminado el introductorio y se sientan preparados para continuar aprendiendo de forma independiente.

