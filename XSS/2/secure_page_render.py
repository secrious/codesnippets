# Secure as title parameter is escaped to make same to prevent injection via unsafe get parameter

def renderMyPage(str):
    content = (''' 
    <html> 
        <body> 
            <h2 id="title">Title -- </h2> 
            <script> 
                titlestr = '%s'; 
                title = document.getElementById('title'); 
                title.innerHTML += titlestr; 
            </script> 
        </body> 
    </html> 
    ''' % str)
    return content

from flask import escape

@app.route('/profile')

def index():
    title = escape(request.args.get('title'))
    page = renderMyPage(title)
    return page