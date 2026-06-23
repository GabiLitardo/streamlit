import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# Leer tus datos reales
data = np.genfromtxt("transfer.txt", delimiter="\t", skip_header=1)
V = data[:, 0]
I = data[:, 1]

st.title("Laboratorio de Pruebas: Componentes de Streamlit")
st.write("Acá podés ver cómo funciona cada control interactivo aplicado a tus datos.")

# Usamos columnas para ordenar los controles y que no quede una lista gigante hacia abajo
col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Selectores de Opciones")
    
    # SELECTBOX: Menú desplegable
    color_linea = st.selectbox(
        "Color de la curva (Selectbox):",
        ["blue", "red", "green", "purple"]
    )
    
    # RADIO: Botones de opción única
    estilo_linea = st.radio(
        "Estilo de línea (Radio):",
        ["Continua (-)", "Discontinua (--)", "Punteada (:)"]
    )

with col2:
    st.subheader("2. Controles Numéricos")
    
    # SLIDER: Barra deslizable (por ejemplo, para cambiar el grosor de la línea)
    grosor = st.slider(
        "Grosor de curva (Slider):", 
        min_value=1, max_value=5, value=2, step=1
    )
    
    # NUMBER INPUT: Casillero numérico con flechas (factor de multiplicación para la corriente)
    multiplicador = st.number_input(
        "Multiplicador de Corriente (Number Input):", 
        min_value=0.5, max_value=10.0, value=1.0, step=0.5
    )

# --- SECCIÓN DE TEXTO ---
st.markdown("---")
st.subheader("3. Entrada de Texto")

# TEXT INPUT: Para que escribas el título dinámicamente
titulo_grafico = st.text_input(
    "Escribí un título personalizado para el gráfico:", 
    value="Mi Curva de Transferencia"
)

# MULTISELECT: Vamos a usarlo para elegir qué elementos extra mostrar en el gráfico
elementos_extra = st.multiselect(
    "Elementos a agregar (Multiselect):",
    ["Grilla de fondo", "Marcadores en los puntos (o)"],
    default=["Grilla de fondo"]
)

# --- PROCESAMIENTO Y DIBUJO DEL GRÁFICO ---
st.markdown("---")

# Mapeamos la selección de texto del 'Radio' a los caracteres que entiende Matplotlib
estilos_dict = {"Continua (-)": "-", "Discontinua (--)": "--", "Punteada (:)": ":"}
line_style = estilos_dict[estilo_linea]

# Creamos la figura aplicando TODAS las variables que modificaste arriba
fig = plt.figure()
plt.title(titulo_grafico)

# Modificamos la corriente por el 'multiplicador' y aplicamos 'color_linea' y 'grosor'
plt.plot(
    V, 
    (1e6 * I) * multiplicador, 
    color=color_linea, 
    linestyle=line_style, 
    linewidth=grosor,
    marker="o" if "Marcadores en los puntos (o)" in elementos_extra else None
)

plt.xlabel("V [V]")
plt.ylabel(r"I [$\mu$A]")

if "Grilla de fondo" in elementos_extra:
    plt.grid(True)

# Renderizar en la web
st.pyplot(fig)
