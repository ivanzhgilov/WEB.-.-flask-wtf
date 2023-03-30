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


@app.route('/list_prof/<display_method>')
def list_prof(display_method):
    list_professions = ["инженер-исследователь", "пилот", "строитель", "экзобиолог", "врач",
                        "инженер по терраформированию", "климатолог", "спеиалист по радиаионной защите", "астролог",
                        "гляциолог", "инженер жизнеобеспечения", "метеоролог", "оператор марсохода", "киберинженер",
                        "штурман", "пилот дронов"]
    return render_template('list_prof.html', list_professions=list_professions, display_methodist=display_method)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    values = {
        'title': "Анкета",
        'surname': "Watny",
        'name': "Mark",
        'education': "выше среднего",
        'profession': "штурман марсохода",
        'sex': "male",
        'motivation': "Всегда мечтал застрять на Марсе!",
        'ready': True
    }
    return render_template('auto_answer.html', **values)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
