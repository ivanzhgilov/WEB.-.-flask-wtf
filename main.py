from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    title = "Загатовка"
    return render_template('base.html', title=title)


@app.route('/training/<prof>')
def training(prof):
    title = "Тренировочный центр"
    if "инженер" in prof or "строитель" in prof:
        professional_orientation = "Инженерные тренажеры"
    else:
        professional_orientation = "Научные симуляторы"
    return render_template('training.html', title=title, professional_orientation=professional_orientation)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
