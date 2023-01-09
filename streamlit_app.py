import streamlit as st
import streamlit_authenticator as stauth

source_pwd = st.text_input('Source password', key='source_pwd', type='password')
if st.button('Hash', key='hash_password'):
    hashed_password = stauth.Hasher([source_pwd]).generate()[0]
    st.text_input('Hashed password', value=hashed_password, key='hashed_password')

st.text_area('AppSecrets', value=st.secrets)
st.write(st.session_state)