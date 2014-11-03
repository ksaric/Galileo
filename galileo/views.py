import flask

from galileo.app import auth, app, manager
from galileo.constants import users
from galileo.helpers import parse_nmap_output
from galileo.model import Network, Computer, Port, Database

# create a blueprint
mod = flask.Blueprint('galileo', __name__)
# mod = flask.Blueprint('networks', __name__, url_prefix='/networks')
# mod = Blueprint('users', __name__, url_prefix='/users')


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@mod.route('/')
def hello_world():
    return flask.render_template('index.html')


def get_upload_file_path(document_filename='scan_network.xml'):
    return app.config['UPLOADED_NMAP_DEST'] + '/' + document_filename


@mod.route('/upload', methods=['GET', 'POST'])
@auth.login_required
def upload():
    if flask.request.method == 'POST':
        file_path = get_upload_file_path()

        upload_file = flask.request.files['nmapXml']
        upload_file.save(file_path)

        # url_for_parse = flask.url_for('parse_document')
        url_for_parse = '/nmap'

        return flask.render_template('show.html', file_path=file_path, url_for_parse=url_for_parse)

    # url_for_upload = flask.url_for('/upload')
    url_for_upload = '/upload'

    return flask.render_template('upload.html', url_for_upload=url_for_upload)


@mod.route('/nmap')
@auth.login_required
def parse_document():
    path = get_upload_file_path()
    xml_content = ""

    with open(path, 'r') as xml_document:
        xml_content = xml_document.read()

    # async NMAP parsing
    parse_nmap_output(xml_content)

    return flask.render_template('scanning.html')

# **********************************
# REST API
# **********************************

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(Network, methods=['GET'])
manager.create_api(Computer, methods=['GET'], results_per_page=500)
manager.create_api(Port, methods=['GET'])
manager.create_api(Database, methods=['GET'])