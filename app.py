# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 08:45:34 2024

@author: jperezr
"""

import streamlit as st



# Estilo de fondo y texto
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    background:
        radial-gradient(black 15%, transparent 16%) 0 0,
        radial-gradient(black 15%, transparent 16%) 8px 8px,
        radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 0 1px,
        radial-gradient(rgba(255,255,255,.1) 15%, transparent 20%) 8px 9px;
    background-color: #282828;
    background-size: 16px 16px;
    color: white;  /* Color del texto general */
    font-size: 24px;  /* Tamaño de letra general */
}
h1, h2, h3, h4, h5, h6 { 
    color: white;  /* Color de los títulos */
    font-size: 24px;  /* Tamaño de letra de los títulos */
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)


# Título del Proyecto
st.title("Prevención de Fraude en Retiros por Desempleo utilizando Inteligencia Artificial en el IMSS y PENSIONISSSTE")

# Sidebar - Nombre
st.sidebar.header("Javier Horacio Pérez Ricárdez")

# Sidebar - ¿Por qué utilizar IA en este tipo de proyectos?
st.sidebar.subheader("¿Por qué utilizar IA en este tipo de proyectos?")
st.sidebar.write("""
La inteligencia artificial (IA) ofrece herramientas avanzadas para detectar patrones inusuales y comportamientos atípicos que podrían indicar fraude. Su capacidad para procesar grandes volúmenes de datos y analizar tendencias en tiempo real permite identificar riesgos antes de que se materialicen, lo que mejora la eficiencia en la prevención de fraudes.
""")

# Sidebar - ¿Por qué utilizar IA en PENSIONISSSTE?
st.sidebar.subheader("¿Por qué utilizar IA en PENSIONISSSTE?")
st.sidebar.write("""
En instituciones como **PENSIONISSSTE**, que gestionan los ahorros de millones de trabajadores, la IA es crucial para proteger estos fondos y garantizar que los retiros por desempleo sean legítimos. Al implementar IA, **PENSIONISSSTE** puede analizar los patrones salariales y detectar posibles fraudes antes de que afecten la estabilidad del sistema.
""")

# Introducción
st.header("Introducción")
st.write("""
El fraude en el sistema de retiro por desempleo es un problema que afecta tanto al **Instituto Mexicano del Seguro Social (IMSS)** como a **PENSIONISSSTE**, dos de las principales instituciones encargadas de gestionar los ahorros y las pensiones de los trabajadores en México.

En los últimos meses, se han identificado casos de fraude en los que los trabajadores declaran salarios más altos de los que realmente perciben, con el fin de realizar retiros por desempleo mayores. Este problema, que afecta el equilibrio del sistema de pensiones, requiere una solución integral que incorpore herramientas de inteligencia artificial (IA) para detectar y prevenir fraudes.
""")

# Objetivo
st.header("Objetivo")
st.write("""
El objetivo de este proyecto es desarrollar un sistema basado en IA para el **IMSS** y **PENSIONISSSTE**, que permita la detección y prevención de fraudes en retiros por desempleo mediante el análisis de patrones salariales, aportaciones y comportamientos sospechosos.
""")

# Descripción del Proyecto
st.header("Descripción del Proyecto")
st.write("""
El proyecto se compone de las siguientes etapas clave, enfocadas en el **IMSS** y **PENSIONISSSTE**:
""")

# Etapas del Proyecto
st.subheader("1. Detección de Anomalías en los Salarios Declarados")
st.write("""
- Descripción: Utilizando modelos de aprendizaje no supervisado, se analizarán los datos de salarios declarados en ambas instituciones para detectar patrones anómalos o discrepancias entre los salarios históricos y los reportados antes de un retiro por desempleo.
- Técnicas:
    - Isolation Forest: Para identificar salarios anómalos.
    - Autoencoders: Detectar comportamientos atípicos en la evolución salarial.
    - Redes Neuronales Recurrentes (RNN): Analizar secuencias temporales de salarios para detectar incrementos inusuales previos a los retiros.
""")

st.subheader("2. Modelos Predictivos para Evaluar el Riesgo de Fraude")
st.write("""
- Descripción: Se desarrollarán modelos predictivos que, utilizando los datos de salarios, aportaciones y retiros por desempleo, clasificarán las solicitudes de retiro en función de su riesgo de fraude.
- Técnicas:
    - Random Forest: Clasificar el riesgo de fraude.
    - Gradient Boosting: Mejorar las predicciones de riesgo.
    - Redes Neuronales: Identificar relaciones complejas entre las variables de los trabajadores.
""")

st.subheader("3. Análisis Comparativo entre Contribuciones y Salarios")
st.write("""
- Descripción: Comparar automáticamente las contribuciones con los salarios declarados en distintos momentos. Discrepancias significativas se reportarán como sospechosas.
- Técnicas:
    - Algoritmos de matching: Comparación de registros para detectar inconsistencias.
    - Análisis de discrepancias: Detección de diferencias en las contribuciones reportadas en distintos periodos.
""")

st.subheader("4. Procesamiento de Lenguaje Natural (NLP) en Comunicaciones")
st.write("""
- Descripción: Se analizarán correos y mensajes entre trabajadores y asesores para identificar indicios de asesorías fraudulentas.
- Técnicas:
    - BERT (Bidirectional Encoder Representations from Transformers): Analizar grandes volúmenes de texto.
    - Análisis de sentimientos: Identificar el tono de las comunicaciones y posibles indicios de fraude.
""")

st.subheader("5. Implementación de Alertas Basadas en Reglas")
st.write("""
- Descripción: Las reglas de negocio permitirán generar alertas automáticas cuando las solicitudes de retiro superen ciertos umbrales o cuando se detecten discrepancias salariales.
- Técnicas:
    - Sistemas basados en reglas: Generación de alertas según políticas específicas.
    - Monitoreo en tiempo real: Verificación de solicitudes de retiro mientras son procesadas.
""")

st.subheader("6. Monitoreo en Tiempo Real")
st.write("""
- Descripción: Integrar la IA en los sistemas del **IMSS** y **PENSIONISSSTE** para monitorear en tiempo real las solicitudes de retiro, validando las contribuciones y salarios declarados antes de la aprobación de cualquier retiro.
- Técnicas:
    - Sistemas de monitoreo en tiempo real: Similares a los utilizados en la banca para prevenir fraudes financieros.
""")

st.subheader("7. Identificación de Redes Fraudulentas")
st.write("""
- Descripción: Utilizando aprendizaje en grafos, se identificarán las relaciones entre trabajadores y asesores previsionales que colaboren en fraudes. Este análisis permitirá detectar redes organizadas que operen de manera recurrente.
- Técnicas:
    - Graph Machine Learning: Análisis de grafos para identificar nodos fraudulentos.
    - Análisis de redes sociales: Identificación de patrones de comportamiento en grupos relacionados con fraudes.
""")

# Recursos Necesarios
st.header("Recursos Necesarios")
st.write("""
- Acceso a datos históricos de salarios y contribuciones del **IMSS** y **PENSIONISSSTE**.
- Casos documentados de fraudes pasados en ambas instituciones para entrenar los modelos.
- Infraestructura tecnológica para el procesamiento de datos en tiempo real.
- Colaboración entre el **IMSS** y **PENSIONISSSTE** para compartir y verificar los datos de contribuciones y salarios.
""")

# Conclusión
st.header("Conclusión")
st.write("""
La colaboración entre el **IMSS** y **PENSIONISSSTE** es fundamental para el éxito de este proyecto, ya que ambas instituciones tienen la responsabilidad de gestionar los fondos de retiro de millones de trabajadores. Utilizando inteligencia artificial y técnicas avanzadas de análisis de datos, el sistema propuesto permitirá detectar y prevenir fraudes en los retiros por desempleo, asegurando que los trabajadores reciban únicamente los montos a los que tienen derecho.
""")

# Referencias
st.header("Referencias")
st.write("""
1. Imagen Radio. (2023). La Consar detecta esquema de fraude en retiros por desempleo. Disponible en: [https://www.imagenradio.com.mx/la-consar-detecta-esquema-de-fraude-en-retiros-por-desempleo](https://www.imagenradio.com.mx/la-consar-detecta-esquema-de-fraude-en-retiros-por-desempleo)

2. López, J. (2021). Inteligencia Artificial aplicada a la prevención de fraudes financieros. Revista de Sistemas Financieros, 18(3), 45-60.

3. Chen, X., & Liu, Y. (2020). Anomaly Detection Using Machine Learning in Financial Transactions. Journal of Machine Learning Applications, 12(2), 101-115.

4. Barredo, E. (2022). El uso de IA en la detección de fraudes en el sector de las pensiones. Revista de Tecnologías Financieras, 27(1), 15-30.

5. Martínez, G., & Gómez, H. (2020). Aprendizaje profundo para la prevención de fraudes en sistemas de retiro por desempleo. Proceedings of the International Conference on AI and Fraud Prevention, 65-72.

6. Zavala, M. (2021). Monitoreo en tiempo real de fraudes en sistemas previsionales. Sistemas de Información Financiera, 35(4), 210-225.
""")

# Sidebar - Botón para descargar el proyecto en PDF
st.sidebar.header("Descargar Proyecto")
with open("fraudes_tex.pdf", "rb") as pdf_file:
    btn = st.sidebar.download_button(
        label="Descargar Proyecto en PDF",
        data=pdf_file,
        file_name="fraudes_tex.pdf",
        mime="application/pdf"
    )


