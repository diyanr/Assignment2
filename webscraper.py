import time
import requests
from config import Config
from forms import SearchForm


from bs4 import BeautifulSoup
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/index', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        target_url = form.website.data
        rowcount = int(form.records.data)
        co_name, co_purpose = getCompany(target_url, rowcount)
        return render_template('index.html', form=form, count=rowcount, company=co_name, purpose=co_purpose)
    return render_template('index.html', form=form)


def getCompany(target_url, count):
    name = []
    purpose = []
    for i in range(count):
        resp = requests.get(target_url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        d = dict(x.string.split(":") for x in soup.find_all('li'))
        name.append(d["Name"])
        purpose.append(d["Purpose"])
        time.sleep(1)
    return name, purpose


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
