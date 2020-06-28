from cgi import parse_qs
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt


html = b"""
<html>
    <body>
        <form action="">
            number1 = <input type="number" name="n1">, 
            number2 = <input type="number" name="n2">  
            <input type="submit">
        </form>
        <img src="/img/result.png" alt="Result image here">
    </body>
</html>
"""



def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    n1 = d.get('n1', [''])[0]
    n2 = d.get('n2', [''])[0]
    if '' not in [n1, n2]:
        n1, n2 = int(n1), int(n2)
        fig = plt.gca()
        fig.axes.get_xaxis().set_visible(False)                                         
        fig.axes.get_yaxis().set_visible(False) 
        plt.text(0.5,0.5,'sum: {}\nproduct: {}' .format(n1 + n2, n1 * n2), horizontalalignment='center', verticalalignment='center', fontsize=28)
        plt.savefig('/var/www/html/img/result.png')
    response_body = html
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]