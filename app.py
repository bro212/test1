import streamlit as st

def perimetro(l1:float, l2:float):
    r = (l1+l2)*2
    return r

def main():
    st.text('suca')
    #slider
    num1 = st.slider('inserisci lato 1:', 0, 100, 20)
    num2 = st.slider('inserisci lato 2:', 0, 100, 20)
    ris_perimetro = perimetro(num1, num2)

    st.write('Il perimetro è: ', ris_perimetro)

if __name__ == '__main__':
    main()