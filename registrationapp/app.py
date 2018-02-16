
from flask import Flask, render_template, Blueprint, request

app = Flask(__name__)
 


@app.route('/')
def index():
     return render_template('home.html')
    

@app.route('/',methods=['GET', 'POST'])
def show():
	if request.method == 'POST':
		if request.form.get('createnote'):
			text = request.form.get('notetext')

			return text

		return render_template('home.html')


# start the server
if __name__ == '__main__':
        app.run(debug=True)