from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_points(speed, speed_limit, is_holiday):
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
            speed = float(request.form['speed'])
            speed_limit = float(request.form['speed_limit'])
            is_holiday = request.form.get('holiday') == 'y'
            points = calculate_points(speed, speed_limit, is_holiday)
            return render_template('index.html', points=points)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
