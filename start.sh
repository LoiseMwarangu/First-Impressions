export SECRET_KEY='Flask WTF Secret Key'

export EMAIL_USERNAME='loisemwarangu@gmail.com'
export EMAIL_PASSWORD='loise@9954'

python3.6 manage.py server
(virtual)$ heroku config:set MAIL_USERNAME='loisemwarangu@gmail.com'
(virtual)$ heroku config:set MAIL_PASSWORD='loise@9954'