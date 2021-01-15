from flask import Flask, url_for, render_template, request, flash
from forms import registerForm
import json, os

app = Flask(__name__)
app.config['SECRET_KEY'] = '0a00dfc1cedfa45766ebedc93622e87f'

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = registerForm()
    if form.validate_on_submit():
        with open('messages.json', 'r+') as file:
            tmp_dict = {form.username.data: form.msg.data}
            if os.stat("messages.json").st_size == 0:
                json.dump(tmp_dict, file)
            else:
                data = json.load(file)
                data.update(tmp_dict)
                file.seek(0)
                json.dump(data, file, indent=2)
        flash('Сообщение записано успешно')
    return render_template('login.html', form=form, title='Валидация')

if __name__ == '__main__':
    app.run(debug=True)
