import io
from flask import Flask, render_template, Response
import processamento
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


app = Flask(__name__)

@app.route('/')
def home():
    describe = processamento.getDescribe()
    head = processamento.getDataHead(10)
    data = [describe, head]

    return render_template("dashboard.html", dados=data)

@app.route('/user')
def user():
    return render_template("user.html")

@app.route('/plot.png')
def plot_png():
    fig = processamento.create_bar()
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


app.run(port=5400, debug=True)