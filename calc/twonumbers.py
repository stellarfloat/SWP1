from cgi import parse_qs
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


n1, n2 = 0, 0
html = f"""
<html>
    <body>
        <form action="">
            number1 = <input type="number" name="n1">, 
            number2 = <input type="number" name="n2">  
            <input type="submit">
        </form>
        sum = {n1 + n2}<br>
        mul = {n1 * n2}
    </body>
</html>
"""



def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    n1 = d.get('n1', [''])[0]
    n2 = d.get('n2', [''])[0]
    if '' not in [n1, n2]:
        n1, n2 = int(n1), int(n2)

    response_body = html
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]