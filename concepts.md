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
