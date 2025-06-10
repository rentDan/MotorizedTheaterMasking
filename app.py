#Flask file to control functions in motor.py and display them on a webpage.

from flask import Flask, render_template
import motor

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', saved_ratios=motor.saved_ratios, 
                           max_steps=motor.max_steps, reset_steps=motor.reset_steps)

@app.route('/reset')
def reset():
    motor.steps_taken = motor.reset(motor.steps_taken)
    return render_template('index.html', saved_ratios=motor.saved_ratios, 
                           max_steps=motor.max_steps, reset_steps=motor.reset_steps)

@app.route('/position/<int:aspect_ratio>')
def position(aspect_ratio):
    motor.steps_taken = motor.position(aspect_ratio, motor.steps_taken)
    return render_template('index.html', saved_ratios=motor.saved_ratios, 
                           max_steps=motor.max_steps, reset_steps=motor.reset_steps)

@app.route('/manual/<direction>/<int:steps_to_take>')
def manual(direction, steps_to_take):
    motor.steps_taken = motor.manual(direction, steps_to_take, motor.steps_taken)
    return render_template('index.html', saved_ratios=motor.saved_ratios, 
                           max_steps=motor.max_steps, reset_steps=motor.reset_steps)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')