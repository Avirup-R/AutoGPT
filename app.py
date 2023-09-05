from __future__ import division
from flask import Flask, render_template, url_for, request, redirect, session, flash, g
import main
import threading

app = Flask(__name__)
app.secret_key = '2' # for flask session


@app.route('/', methods = ['GET'])
def home_page():
        return render_template('home_page.html')

@app.route('/youtube', methods=['GET', 'POST'])
def youtube():
        if request.method=='GET':
                return render_template('youtube_page.html')
        elif request.method=='POST':
                code=request.form['code']
                thread = threading.Thread(target=main.video_summarizer, args=(code))
                thread.start()
                output=main.video_summarizer(code)
                thread.join()
                print(output)
                return render_template('youtube_page_2.html', messages=output)
        
@app.route('/web_search', methods=['GET', 'POST'])
def web_search():
        if request.method=='GET':
                return render_template('web_search_page.html')
        elif request.method=='POST':
                q=request.form['q']
                thread = threading.Thread(target=main.online_search, args=(q))
                thread.start()
                output=main.online_search(q)
                thread.join()
                return render_template('web_search_page_2.html', messages=output)
        

@app.route('/code_completion', methods=['GET', 'POST'])
def code_completion():
        if request.method=='GET':
                return render_template('code_completion_page.html')
        elif request.method=='POST':
                t=request.form['t']
                thread = threading.Thread(target=main.code_completion, args=(t))
                thread.start()
                output=main.code_completion(t)
                thread.join()
                return render_template('code_completion_page_2.html', messages=output)
        


if __name__ == '__main__':
    app.run(debug=True)
                