import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#defino las columnas que me interesan
fields = ['course_id', 'course_title', 'price', 'num_subscribers', 'num_lectures', 'level']
df = pd.read_csv('Udemy.csv', usecols= fields)


st.title('Visualización de datos de Udemy')
st.subheader('Principales componentes')
st.markdown('***')

if st.checkbox("Mostrar dataframe Udemy"):
    if st.button('Mostrar head'):
        st.write(df.head())
    if st.button('Mostrar tail'):
        st.write(df.tail())

st.subheader('Información de dimensiones de la data de Udemy')

dim = st.radio('Dimensiónm a mostrar:', ('Filas', 'Columnas'),horizontal=True)
if dim == 'Filas':
    st.write('Cantidad de filas:', df.shape[0])
else:
    st.write('Cantidad de columnas:', df.shape[1])

st.markdown('***')
st.header("Qué es la correlación ?")
st.write("Contexto: La correlación es un tipo de asociación entre dos variables numéricas, específicamente evalúa la tendencia (creciente o decreciente) en los datos. ")
st.markdown('***')
st.header('Análisis de datos de UDEMY')

precio_limite = st.slider('Definir precio máximo',0,200,0)
st.markdown("Análisis gráfico del aumento de precios con respecto al número de lecturas")
fig = plt.figure(figsize=(6,4))
sns.scatterplot(x= 'price', y = 'num_lectures', data=df[df['price']<precio_limite])
st.pyplot(fig)

st.markdown('***')

st.header("El curso que más se ha leido, se podria decir que este es el mejor curso es:")

st.write(df.loc[df.num_lectures.idxmax()] )

st.markdown('***')

st.markdown("Calculamos la correlación entre el precio y número de lecturas")

st.write("Correlación:", df['price'].corr(df['num_lectures']))

st.markdown("El coeficiente de correlación es 0.3301604481628124. Dado que esta correlación es positiva, nos dice que los precios y los números de lecturas están correlacionados positivamente. En otras palabras, a medida que aumentan los valores en la columna de precios, los valores en la columna de número de lecturas tienden a aumentar.")

st.markdown('***')
st.markdown("Análisis gráfico del aumento de precios con respecto al número de suscriptores")
fig2 = plt.figure(figsize=(6,4))
sns.scatterplot(x= 'price', y = 'num_subscribers', data=df[df['price']<precio_limite])
st.pyplot(fig2)

st.markdown("Calculamos la correlación entre el precio y número de suscriptores")

st.write("Correlación:", df['price'].corr(df['num_subscribers']))

st.markdown("El coheficiente de correlación es de 0.05076934882586656. Las columnas price y número de suscriptores se correlacionan positivamente. Mientras que más aumentan los precios aumentan el numero de suscriptores, hablando coloquialmente una parte de la población esta dispuesta a pagar más o suscribirse en un curso de buena calidad, como dice el dicho lo barato sale caro, por esto la gente siempre busca la mejor marca o aquel producto que le ofrezca mucho más de lo que le ofrece otros productos. En nuestro analisis no quiere decir que los cursos que valen aproximadamente 25$ sean malos, no!, ya que hay una buena cantidad de personas que han pagado por estos cursos, sin embargo hay una parte de la población que compran y se suscriben a los cursos de mayor valor porque buscan algo más que solo lo basico, por ejemplo los clientes buscan cursos que no solo le den las clases del curso en vivo o grabadas, también buscan variables donde el curso ofrezca certificación o que sean para aprender las habilidades más demandadas en el mercado actual.")

st.markdown('***')

#defino las columnas que me interesan
fields2 = ['title', 'level', 'language', 'subtitles', 'price', 'n_enrolled']
df_edx = pd.read_csv('edx.csv', usecols= fields2)

st.title('Visualización de datos de Edx')
st.subheader('Principales componentes')
st.markdown('***')

if st.checkbox("Mostrar dataframe Edx"):
    if st.button('Mostrar head'):
        st.write(df_edx.head())
    if st.button('Mostrar tail'):
        st.write(df_edx.tail())


st.subheader('Información de dimensiones de la data de Edx')

dim2 = st.radio('Dimensión a mostrar:', ('filas', 'columnas'),horizontal=True)
if dim2 == 'filas':
    st.write('Cantidad de filas:', df_edx.shape[0])
else:
    st.write('Cantidad de columnas:', df_edx.shape[1])

st.markdown('***')


st.header("Análisis de datos de EDX")


precio_limite2 = st.slider('Definir precio máximo',0,299,0)

st.markdown("Análisis gráfico del aumento de precios con respecto al número de estudiantes inscriptos")
figura = plt.figure(figsize=(6,4))
sns.scatterplot(x= 'price', y = 'n_enrolled', data=df_edx[df_edx['price']<precio_limite2])
st.pyplot(figura)


st.markdown('***')

st.header("Observamos los datos del curso con más estudiantes inscritos")

st.write(df_edx.loc[df_edx.n_enrolled.idxmax()])

st.markdown('***')


st.markdown("Calculamos la correlación entre el precio y número de estudiantes inscriptos")

st.write("Correlación:", df_edx['price'].corr(df_edx['n_enrolled']))


st.markdown("El coeficiente de correlación es -0.009482190720812004 .Esta correlación es negativa, nos dice que los puntos y las asistencias están correlacionados negativamente. Esto quiere decir que a medida que aumentan los valores en la columna de precios, los valores en la columna de numero de inscristos tienden a disminuir.")

st.markdown("***")

st.bar_chart(data=df_edx,  x='level', y='n_enrolled',use_container_width=True)

st.markdown("Se podria interpretar que a medida que el nivel de los cursos cambian a categorias más avanzadas suelen haber menos estudiantes inscriptos, la razón de esto se debe a que muchos estudiantes no habrán terminado el introductorio, o también que hayan terminado el introductorio y se sientan preparados para continuar aprendiendo de forma independiente. También se debe a como se vio anteriormente en la correlación ya que mientras mas avanzado sea el nivel más costosos son los cursos y por ende en esta plataforma suelen disminuir el número de estudiantes al terminar el nivel introductorio")


