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
html_initial = """
<html>
    <body>
        <form action="">
            number1 = <input type="number" name="n1">, 
            number2 = <input type="number" name="n2">  
            <input type="submit">
        </form>
        <br>값을 입력하세요.
    </body>
</html>
"""
html_error = """
<html>
    <body>
        <form action="">
            number1 = <input type="number" name="n1">, 
            number2 = <input type="number" name="n2">  
            <input type="submit">
        </form>
        오류 : {}
    </body>
</html>
"""



def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    n1 = d.get('n1', [''])[0]
    n2 = d.get('n2', [''])[0]
    if '' not in [n1, n2]:
        try:
            n1, n2 = int(n1), int(n2)
            response_body = html
        except ValueError:
            error_msg = '잘못된 값이 입력되었습니다. 입력된 값이 숫자인지 다시 확인해보세요.'
            response_body = html_error .format(error_msg)
        except Exception:
            error_msg = '알 수 없는 오류가 발생했습니다. 서버 관리자에게 문의하세요.'
            response_body = html_error .format(error_msg)
    else:
        response_body = html_initial

    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]