def format_response(response):
    return response.strip()

def manage_session_state(key, default_value=None):
    if key not in st.session_state:
        st.session_state[key] = default_value

def clear_session_state():
    for key in list(st.session_state.keys()):
        del st.session_state[key]