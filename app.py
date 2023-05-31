from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def solution():
    a = float(request.form.get('a'))
    b = float(request.form.get('b'))
    c = float(request.form.get('c'))
    discriminant = b**2-4*a*c
    if discriminant < 0:
        return render_template('result.html', result='Квадратное уравнение не имеет действительных корней')
    elif discriminant == 0:
        x=-b/(2*a)
        return render_template('result.html',result=f'Квадратное уравнение имеет один корень: x={x}')
    else:
        x1 = (-b-discriminant**0.5)/(2*a)
        x2 = (-b + discriminant ** 0.5) / (2 * a)
        return render_template('result.html',result=f'Квадратное уравнение имеет два корня: x1={x1} и x2={x2}')

if __name__ == '__main__':
    app.run()