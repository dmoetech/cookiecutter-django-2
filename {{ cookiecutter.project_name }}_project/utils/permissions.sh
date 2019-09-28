chown -R root:www-data /home/{{ cookiecutter.project_name }}_project
chmod -R 750 /home/{{ cookiecutter.project_name }}_project
find /home/{{ cookiecutter.project_name }}_project -type f -print0|xargs -0 chmod 740
chmod -R 770 /home/{{ cookiecutter.project_name }}_project/{{ cookiecutter.project_name }}/{{ cookiecutter.project_name }}/media
find /home/{{ cookiecutter.project_name }}_project/{{ cookiecutter.project_name }}/{{ cookiecutter.project_name }}/media -type f -print0|xargs -0 chmod 760
chmod 770 /home/{{ cookiecutter.project_name }}_project/{{ cookiecutter.project_name }}/logs
chmod -R 760 /home/{{ cookiecutter.project_name }}_project/{{ cookiecutter.project_name }}/logs/*
chmod 770 /home/{{ cookiecutter.project_name }}_project/{{ cookiecutter.project_name }}
chmod -R 760 /home/{{ cookiecutter.project_name }}_project/{{ cookiecutter.project_name }}/db.sqlite3
