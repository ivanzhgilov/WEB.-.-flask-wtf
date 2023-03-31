from flask import Flask, render_template
from forms.emergency_access import EmergencyAccess
from flask import redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = EmergencyAccess()
    access = False
    if form.validate_on_submit():
        access = True
    return render_template('login.html', title='Авторизация', form=form, access=access)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
