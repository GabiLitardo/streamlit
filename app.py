import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Configuración del título de la página web
st.title("Visualizador de Curvas de Transferencia")
st.write("Carga tu archivo `.txt` para graficar los datos de voltaje e corriente.")

# Componente interactivo para subir el archivo txt
uploaded_file = st.file_uploader("Elige tu archivo transfer.txt", type=["txt"])

if uploaded_file is not None:
    # Leemos los datos directamente del archivo subido
    data = np.genfromtxt(uploaded_file, delimiter="\t", skip_header=1)
    
    V = data[:, 0]
    I = data[:, 1]
    
    # Creamos el gráfico con Matplotlib de la misma forma que lo tenías
    fig, ax = plt.subplots()
    ax.set_title("Transferencia")
    ax.plot(V, 1e6 * I, marker='o', color='b')
    ax.set_xlabel("V [V]")
    ax.set_ylabel(r"I [$\mu$A]")
    ax.grid(True) # Un toque extra para que se vea más profesional
    
    # En Streamlit usamos st.pyplot pasando la figura creada
    st.pyplot(fig)
    
    # Bonus: También puedes mostrar los datos en una tabla interactiva si quieres
    if st.checkbox("Mostrar tabla de datos"):
        st.dataframe(data, column_config={0: "Voltaje (V)", 1: "Corriente (A)"})
else:
    st.info("Por favor, sube un archivo de texto para ver la gráfica.")
