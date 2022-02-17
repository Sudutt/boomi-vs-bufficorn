from flask import render_template
from .covalent_api import random_nft_data

from . import app


@app.route('/', methods=['GET'])
def index():
    return render_template('entry.html')


@app.route('/arena', methods=['GET'])
def entry():
    boomi_add = "0xF3402D09BfF30252872ec60A00305E3fD082A701"
    boomi_cid = "137"
    boomi_orig = random_nft_data(boomi_add, boomi_cid)
    bufficorn_add = "0x1e988ba4692e52Bc50b375bcC8585b95c48AaD77"
    bufficorn_cid = "1"
    bufficorn_orig = random_nft_data(bufficorn_add, bufficorn_cid)
    kwargs = dict()
    kwargs['boomi_name'] = boomi_orig['name']
    kwargs['boomi_url'] = boomi_orig['image_url']
    kwargs['boomi_desc'] = boomi_orig['description']
    for attr in boomi_orig['attributes']:
        key = attr['trait_type'].lower()
        kwargs['boomi_'+key] = attr['value']
    kwargs['bufficorn_name'] = bufficorn_orig['name']
    kwargs['bufficorn_url'] = bufficorn_orig['image_url']
    kwargs['bufficorn_desc'] = bufficorn_orig['description']
    for attr in bufficorn_orig['attributes']:
        key = attr['trait_type'].lower()
        kwargs['bufficorn_'+key] = attr['value']
    return render_template('index.html', **kwargs)
