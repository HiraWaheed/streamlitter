# Streamlit Concepts Notes 
- basic concepts like write,columns
- built-in functions like radio, input fields, buttons,checkbox, dropdown lists
- advanced concepts
    - sessions
        - Session State associates stored values to keys (strings). Values in session state are only available in the single session where it was saved.
    - caching (2 types decorator: @cache_data, @cache_resource)
        - @cache_data: to cache computations that return data
        - @cache_resource: to cache global resources like ML models or database connections.
        - Caching associates stored values to specific functions and inputs. Cached values are accessible to all users across all sessions.
    - fragments
        - Fragments help prevent reruns of the whole app. The part of app that uses 
        @st.fragment() decorator is only re-run instead of the whole app.  
        - forms vs fragments: A fragment immediately processes user input but limits the scope of the rerun. Whereas a form batches user input without interaction between any widgets  
        - fragments vs cache: Caching saves you from unnecessarily running a piece of your app while the rest runs. Fragments save you from running your full app when you only want to run one piece.  
        
# Documentation
https://docs.streamlit.io/get-started/
