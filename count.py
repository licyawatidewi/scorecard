import math
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))


def dealergr(dealergroup):
    if dealergroup == "AJM":
        dealer = 1
    elif dealergroup == "ANDALAN":
        dealer = 2
    elif dealergroup == "ARISTA":
        dealer = 3
    elif dealergroup == "":
        dealer = 4
    elif dealergroup == "BLSS":
        dealer = 5
    elif dealergroup == "EUROKARS":
        dealer = 6
    elif dealergroup == "HANAWA":
        dealer = 7
    elif dealergroup == "":
        dealer = 8
    elif dealergroup == "KUMALA":
        dealer = 9
    elif dealergroup == "MAJU MOTOR":
        dealer = 10
    elif dealergroup == "MIMOSA":
        dealer = 11
    elif dealergroup == "NUSANTARA":
        dealer = 12
    elif dealergroup == "PERDANA":
        dealer = 13
    elif dealergroup == "PRIMA":
        dealer = 14
    elif dealergroup == "":
        dealer = 15
    elif dealergroup == "":
        dealer = 16
    else:
        dealer = 17

    return dealer


def modelspa(model, salespoint):
    if (model == 'ALMAZ' or model == 'CORTEZ' or model == 'FORMO' or model == 'HS' or model == 'ZS') \
            and (salespoint == 'DKI 1' or salespoint == 'DKI 2' or salespoint == 'DKI 3' or salespoint == 'JABAR'):
        modelsp = 1
    elif (model == 'ALMAZ' or model == 'CORTEZ' or model == 'FORMO' or model == 'HS' or model == 'ZS') \
            and (salespoint == 'JATENG' or salespoint == 'JATIM 1, BALI, LOMBOK' \
            or salespoint == 'JATIM 2' or salespoint == 'KALIMANTAN' or salespoint == 'SULBAGSEL' \
            or salespoint == 'SULBAGUT' or salespoint == 'SUMBAGSEL' or salespoint == 'SUMBAGUT'):
        modelsp = 2
    elif model == 'CONFERO' and (salespoint == 'DKI 1' or salespoint == 'JABAR'):
        modelsp = 2
    elif model == 'CONFERO' and (salespoint == 'SULBAGSEL' or salespoint == 'SULBAGUT'):
        modelsp = 4
    else:
        modelsp = 3

    return modelsp


def modelsparea(model, salespoint):
    if (model == 1 or model == 3 or model == 4 or model == 5 or model == 6) \
            and (salespoint == 1 or salespoint == 2 or salespoint == 3 or salespoint == 5):
        modelsp = 1
    elif (model == 1 or model == 3 or model == 4 or model == 5 or model == 6) \
            and (salespoint == 6 or salespoint == 7 \
            or salespoint == 8 or salespoint == 9 or salespoint == 10 \
            or salespoint == 11 or salespoint == 12 or salespoint == 13):
        modelsp = 2
    elif model == 2 and (salespoint == 1 or salespoint == 5):
        modelsp = 2
    elif model == 2 and (salespoint == 10 or salespoint == 11):
        modelsp = 4
    else:
        modelsp = 3

    return modelsp


def maritalstat(maritalstatus):
    if maritalstatus == "DIVORCE":
        marital = 1
    elif maritalstatus == "DUDA":
        marital = 2
    elif maritalstatus == "MARRIED":
        marital = 3
    elif maritalstatus == "SINGLE":
        marital = 4
    else:
        marital = 5

    return marital


def wcalimit(wca):
    if wca > 210:
        wcalim = 210
    else:
        wcalim = wca

    return wcalim


def w12malimit(w12ma):
    if w12ma > 210:
        w12malim = 210
    else:
        w12malim = w12ma

    return w12malim


def logapdoc(pdoc):
    if pdoc == 0:
        logpdoc = 0
    else:
        logpdoc = math.log(pdoc, 10)
    return logpdoc


def jobcat(job_cat):
    if job_cat == "ENTREPRENEUR":
        job = 1
    elif job_cat == "NON-ENTREPRENEUR":
        job = 2

    return job


def asset_cal(assettype):
    if assettype == "ALMAZ EXC":
        asset = 1
    elif assettype == "ALMAZ":
        asset = 2
    elif assettype == "ALMAZ SE":
        asset = 3
    elif assettype == "CONFERO":
        asset = 4
    elif assettype == "CORTEZ CT":
        asset = 5
    elif assettype == "CORTEZ S":
        asset = 6
    elif assettype == "FORMO":
        asset = 7
    elif assettype == "HS":
        asset = 8
    elif assettype == "ZS":
        asset = 9
    return asset


def asset_segment(assettype):
    if assettype == "FORMO" or assettype == "CONFERO" or assettype == "CORTEZ S":
        segment = 1
    elif assettype == "ZS" or assettype == "ALMAZ SE" or assettype == "CORTEZ CT":
        segment = 2
    elif assettype == "HS" or assettype == "ALMAZ EXC" or assettype:
        segment = 3
    return segment


def pay(paymenttype):
    if paymenttype == "ADVANCE":
        payment = 1
    else:
        payment = 2
    return payment


def sparea(salespoint):
    if salespoint == "DKI 1":
        sp = 1
    elif salespoint == "DKI 2":
        sp = 2
    elif salespoint == "DKI 3":
        sp = 3
    elif salespoint == "DKI 4 (MG)":
        sp = 4
    elif salespoint == "JABAR":
        sp = 5
    elif salespoint == "JATENG":
        sp = 6
    elif salespoint == "JATIM 1, BALI, LOMBOK":
        sp = 7
    elif salespoint == "JATIM 2":
        sp = 8
    elif salespoint == "KALIMANTAN":
        sp = 9
    elif salespoint == "SULBAGSEL":
        sp = 10
    elif salespoint == "SULBAGUT":
        sp = 11
    elif salespoint == "SUMBAGSEL":
        sp = 12
    elif salespoint == "SUMBAGUT":
        sp = 13

    return sp


def dealerspa(dealer, salespoint):
    if (dealer == "AJM" or dealer == "ANDALAN" or dealer == "ARISTA" or dealer == "EUROKARS" or dealer == "MAJU MOTOR" or \
        dealer == "MIMOSA" or dealer == "NUSANTARA" or dealer == "PERDANA" or dealer == "PRIMA" or dealer == "TPM") \
        and (salespoint == "DKI 1" or salespoint == "DKI 2" or salespoint == "JABAR"):
        dealersp = 1
    elif (dealer == "BLSS") and (salespoint == "DKI 1" or salespoint == "DKI 2" or salespoint == "DKI 3" or salespoint == "JABAR"\
            or salespoint == "JATENG" or salespoint == "JATIM 1, BALI, LOMBOK" or salespoint == "JATIM 2" \
            or salespoint == "SULBAGUT" or salespoint == "SUMBAGSEL" or salespoint == "SUMBAGUT"):
        dealersp = 2
    elif (dealer == "AJM" or dealer == "ANDALAN" or dealer == "ARISTA" or dealer == "EUROKARS" or \
        dealer == "MIMOSA" or dealer == "NUSANTARA" or dealer == "PERDANA" or dealer == "PRIMA" or dealer == "TPM") \
            and (salespoint == "JATENG" or salespoint == "JATIM 1, BALI, LOMBOK" or salespoint == "JATIM 2" \
            or salespoint == "SULBAGUT" or salespoint == "SUMBAGSEL" or salespoint == "SUMBAGUT" or salespoint == \
            "KALIMANTAN" or salespoint == "SULBAGUT"):
        dealersp = 2
    elif (dealer == "BLSS" or dealer == "HANAWA" or dealer == "KUMALA") and (salespoint == "KALIMANTAN" or salespoint == "SULBAGSEL"):
        dealersp = 5
    elif dealer == "ARISTA" or dealer == "PRIMA" or dealer == "MAJU MOTOR" and salespoint == "DKI 3":
        dealersp = 5
    else:
        dealersp = 4

    return dealersp


def dpandotr(dp, otr):
    if dp > 25.23:
        dpotr = 1
    elif dp <= 25.23 and otr <= 147800000:
        dpotr = 2
    else:
        dpotr = 3
    return dpotr


def trendstat(trendset):
    if trendset == "UP":
        trend = 1
    elif trendset == "DOWN":
        trend = 3
    else:
        trend = 2
    return trend


def logatcc(tcc):
    if tcc == 0:
        logtcc = 0
    else:
        logtcc = math.log(tcc, 10)
    return logtcc


def logapdcc(pdcc):
    if pdcc == 0:
        logpdcc = 0
    else:
        logpdcc = math.log(pdcc, 10)
    return logpdcc


def nohitcount(nohitstat):
    if nohitstat == "nohit":
        nohit = 1
    else:
        nohit = 0
    return nohit


def hitnoscorecount(hitnoscorestat):
    if hitnoscorestat == "noscore":
        hitnoscore = 1
    else:
        hitnoscore = 0
    return hitnoscore
