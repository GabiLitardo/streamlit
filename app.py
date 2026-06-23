import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

# La única modificación de origen: toma el archivo desde la ruta local "transfer.txt"
data = np.genfromtxt("transfer.txt", delimiter = "\t", skip_header = 1)
V = data[:, 0]
I = data[:, 1]

plt.figure()
plt.title("Transferencia")
plt.plot(V, 1e6*I)
plt.xlabel("V [V]")
plt.ylabel(r"I [$\mu$A]")

# Reemplazamos plt.show() por st.pyplot() para que se muestre en la web
st.pyplot(plt.gcf())
