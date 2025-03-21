import streamlit as st
import numpy as np

# Funktion zur Berechnung der Lagebeziehung
def check_lagebeziehung(a1, b1, a2, b2):
    a1, b1, a2, b2 = np.array(a1), np.array(b1), np.array(a2), np.array(b2)

    # Überprüfung auf Parallelität
    if np.linalg.matrix_rank(np.column_stack((b1, b2))) == 1:
        if np.linalg.matrix_rank(np.column_stack((b1, a2 - a1))) == 1:
            return "Die Geraden sind identisch."
        else:
            return "Die Geraden sind parallel."

    # Überprüfung auf Schnittpunkt
    A = np.column_stack((b1, -b2))
    try:
        lambdas = np.linalg.solve(A, a2 - a1)
        schnittpunkt = a1 + lambdas[0] * b1
        return f"Die Geraden schneiden sich in {schnittpunkt}."
    except np.linalg.LinAlgError:
        return "Die Geraden sind windschief."

# Streamlit App UI
st.title("Lagebeziehung von zwei Geraden")

st.write("Gib die Punkte und Richtungsvektoren als Listen ein (z.B. `1,2,3`)")

a1 = st.text_input("Punkt A1 (Aufpunkt der 1. Geraden)", "1,2,3")
b1 = st.text_input("Richtungsvektor B1", "2,3,4")
a2 = st.text_input("Punkt A2 (Aufpunkt der 2. Geraden)", "4,5,6")
b2 = st.text_input("Richtungsvektor B2", "1,1,1")

if st.button("Berechnen"):
    try:
        a1 = list(map(float, a1.split(",")))
        b1 = list(map(float, b1.split(",")))
        a2 = list(map(float, a2.split(",")))
        b2 = list(map(float, b2.split(",")))

        result = check_lagebeziehung(a1, b1, a2, b2)
        st.success(result)

    except Exception as e:
        st.error(f"Fehler bei der Eingabe: {e}")
