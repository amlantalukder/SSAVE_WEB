import uuid, pdb
from web_version.controller import WebUIController
from flask import render_template, redirect, request, jsonify, url_for
from web_version import app

print(id(app))

@app.route('/', methods=['GET'])
def home():
    app.logger.info('Home page loaded.')
    job_id = uuid.uuid4().hex
    return render_template('index.html', job_id=job_id)

@app.route('/config/<job_id>', methods=['GET'])
def config(job_id):
    print(job_id)

    controller = WebUIController(app, job_id)

    status, msg, data = controller.getConfig()
    
    app.logger.info(msg)

    channel_settings, \
    annots_left_settings, annots_right_settings, sleep_stages, \
    filter_settings, bad_annot_settings = data
    
    app.logger.info('Configurations loaded.')
    return render_template('config.html', job_id = job_id, \
                                            channel_settings=channel_settings, 
                                            annots_left_settings=annots_left_settings,
                                            annots_right_settings=annots_right_settings,
                                            sleep_stages=sleep_stages,
                                            filter_settings=filter_settings,
                                            bad_annot_settings=bad_annot_settings)

@app.route('/load/<job_id>', methods = ['POST'])
def loadData(job_id):
    print(job_id)
    controller = WebUIController(app, job_id)
    app.logger.info(f'Data load request: {request}')
    response = controller.loadSleepData(request)
    app.logger.info(f'Data load response: {response}')
    return jsonify(response)

@app.route('/execute/<job_id>', methods = ['POST'])
def execute(job_id):
    print(job_id)
    controller = WebUIController(app, job_id)
    app.logger.info(f'Execution request: {request}')
    response = controller.execute(request)
    app.logger.info(f'Execution response: {response}')
    return jsonify(response)

@app.route('/savesettings/<job_id>', methods = ['POST'])
def saveSettings(job_id):
    print(job_id)
    controller = WebUIController(app, job_id)
    app.logger.info(f'Save settings request: {request}')
    response = controller.saveSettings(request)
    app.logger.info(f'Save settings response: {response}')
    return jsonify(response)

@app.route('/download/<job_id>', methods = ['GET'])
def download(job_id):
    print(job_id)
    controller = WebUIController(app, job_id)
    app.logger.info(f'Download request')
    response = controller.download()
    app.logger.info(f'Download response: {response}')
    return jsonify(response)