<VirtualHost 127.0.0.1:8089>
	ServerAdmin kwan@media.mit.edu
	ServerName  powerally.com
	ServerAlias powerally.com 
	
	# Indexes + Directory Root.
	DirectoryIndex index.html
	DocumentRoot /home/www/powerally.com/htdocs/

	WSGIDaemonProcess powerally.com python-path=/home/virtualenv/powerenv/lib/python2.6/site-packages
	WSGIProcessGroup powerally.com

	WSGIScriptAlias / /home/www/powerally.com/electrify/apache/wsgi.py

	<Directory /home/www/powerally.com/electrify/apache>
	    <Files wsgi.py>
		Order deny,allow
		Allow from all
	    </Files>
	</Directory>

	# Logfiles
	ErrorLog  /home/www/powerally.com/logs/error.log
	CustomLog /home/www/powerally.com/logs/access.log combined
</VirtualHost>

