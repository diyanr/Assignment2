import time
import requests
import pandas as pd
from config import Config
from forms import SearchForm, ResultForm

from bs4 import BeautifulSoup
from flask import Flask, session
from flask import render_template, Response

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/index', methods=['GET', 'POST'])
def search():
    s_form = SearchForm()
    r_form = ResultForm()
    co_info = pd.DataFrame()
    if s_form.validate_on_submit():
        target_url = s_form.website.data
        rowcount = int(s_form.records.data)
        co_info = getCompany(target_url, rowcount)
        session['co_info'] = co_info
        return render_template('index.html', form1=s_form, form2=r_form, company=co_info)
    elif r_form.validate_on_submit():
        if 'co_info' in session:
            co_info = session['co_info']
            csv_data = co_info.to_csv(index=False)
            return Response(csv_data, mimetype="text/csv",
                            headers={"Content-disposition": "attachment; filename=mydata.csv"})
    return render_template('index.html', form1=s_form)


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
    return pd.DataFrame({"name": name, "purpose": purpose})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
