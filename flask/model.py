import ctypes
import xgboost
import xgboost.core
import pandas as pd
import flask
from count import modelsparea, logapdoc, wcalimit, w12malimit

def xgb_load_model(buf):
    if isinstance(buf, str):
        buf = buf.encode()
    bst = xgboost.core.Booster()
    n = len(buf)
    length = xgboost.core.c_bst_ulong(n)
    ptr = (ctypes.c_char * n).from_buffer_copy(buf)
    xgboost.core._check_call(
        xgboost.core._LIB.XGBoosterLoadModelFromBuffer(bst.handle, ptr, length)
    )
    return bst

with open('xgb6.model', 'rb') as f:
    raw = f.read()

model = xgb_load_model(raw)
print(model)

def model6(dealer, modelsp, dp, tenor, otr, marital, pefindo, wca, w12ma, pdoc):

    with open('xgb6.model', 'rb') as f:
        raw = f.read()

    model = xgb_load_model(raw)
    print(model)

    column_names = ['Dealer_Group_Use', 'Model_SP_Use', 'DP', 'Tenor Use',
                    'OTR', 'Marital Status Use', 'Pefindo Score Use', 'WCA_lim',
                    'W12MA_lim', 'LOG_PDOC']

    new_row = [dealer, modelsp, dp, tenor, otr, marital, pefindo, wca, w12ma, pdoc]
    print(new_row)
    df = pd.DataFrame(columns=column_names)
    df.loc[len(df)] = new_row
    dftest = xgboost.DMatrix(df)
    prob = model.predict(dftest)
    print('The PD is: ', prob[0])
    return prob[0]

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return (flask.render_template('main.html'))

    if flask.request.method == 'POST':
        dp_var = float(flask.request.form['dp_var'])
        tenor_var = float(flask.request.form['tenor_var'])
        otr_var = float(flask.request.form['otr_var'])
        marital_var = int(flask.request.form['marital_var'])
        sp_var = int(flask.request.form['sp_var'])
        dealer_var = int(flask.request.form['dealer_var'])
        model_var = int(flask.request.form['model_var'])
        pefindo_var = float(flask.request.form['pefindo_var'])
        wca_var = int(flask.request.form['wca_var'])
        w12ma_var = int(flask.request.form['w12ma_var'])
        pdoc_var = float(flask.request.form['pdoc_var'])

        modelsp = modelsparea(model_var, sp_var)
        wcalim = wcalimit(wca_var)
        w12malim = w12malimit(w12ma_var)
        logpdoc = logapdoc(pdoc_var)

        res = model6(dealer_var, modelsp, dp_var, tenor_var, otr_var, marital_var,
                     pefindo_var, wcalim, w12malim, logpdoc)
        result = (1-res)
        pred = result*100
        prediction = round(pred, 2)

        return flask.render_template('main.html',
                                     result=prediction, )


if __name__ == '__main__':
    app.run()