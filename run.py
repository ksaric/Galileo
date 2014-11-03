__author__ = 'ksaric'

from galileo import app

app.db.drop_all()
app.db.create_all()

app.app.run(debug=True, host='0.0.0.0')

