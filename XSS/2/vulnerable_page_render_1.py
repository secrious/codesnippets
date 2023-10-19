# Vulnerable as `\` is a simple restriction which can be avoided using `img` or other techniques
# and weak code sanitisation uses replace, better methods such as whitelisting are more secure

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
    title = request.args.get('title')
    title = title.replace('\'', '', -1)
    page = renderMyPage(title)
    return page