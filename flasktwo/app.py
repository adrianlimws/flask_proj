from flask import Flask, render_template, request

app = Flask(__name__)


def cal_demerit_points(speed, speed_limit, is_holiday):
    if speed <= speed_limit:
        return 0
    else:
        difference = speed - speed_limit
        points = difference // 5
        if is_holiday:
            points *= 2
        return points


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'reset' in request.form:
            return render_template('index.html')
        else:
            speed_input = request.form['speed']
            speed_limit_input = request.form['speed_limit']
            is_holiday = request.form.get('holiday') == 'y'
            try:
                speed = float(speed_input)
                speed_limit = float(speed_limit_input)
            except ValueError:
                error_message = 'Please enter valid speed number.'
                return render_template('index.html', error_message=error_message)
            else:
                points = cal_demerit_points(speed, speed_limit, is_holiday)
                return render_template('index.html', points=points)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
