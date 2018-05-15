import os
from weblist import create_app

app = create_app('ConfigPro'
                 if os.environ.get('WEBLIST_MODE') == 'pro' else 'ConfigDev')

if __name__ == '__main__':
    app.run(
        host=app.config.get('HOST'),
        port=app.config.get('PORT'),
        debug=app.config.get('DEBUG')
    )
