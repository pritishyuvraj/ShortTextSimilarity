from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
	return 'Sentences-> %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		s1 = request.form['sent1']
		s2 = request.form['sent2']
		s3 = s1 + "\n" + s2 
		if s1 and s2:
			write2file(s1, s2)
			print s1, s2 
		return redirect(url_for('success',name = s3))
	else:
		user = request.args.get('nm')
		return redirect(url_for('success',name = user))

def write2file(S1, S2):
    text = "python sts1.py \"" + S1 + "\" \"" + S2 + " \""
    open('script.sh', 'w').close()
    f = open('script.sh', 'w')
    f.write(text)
    f.close()
    print "Done Writing"

    from subprocess import call
    call(['sh', 'script.sh'])
    
if __name__ == '__main__':
		app.run(debug = True)