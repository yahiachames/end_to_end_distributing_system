FROM python:3.9
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY . .  
RUN apt update && apt-get install -y python3-pip python3-venv apache2 libapache2-mod-wsgi-py3
RUN pip install -r requirements.txt
RUN mkdir -p /var/www/static

# Set up Apache for Django
COPY django_project.conf /etc/apache2/sites-available/
RUN a2ensite django_project && a2dissite 000-default.conf
RUN a2enmod rewrite

# Collect static files
RUN python manage.py collectstatic --noinput

EXPOSE 80
CMD ["apache2ctl", "-D", "FOREGROUND"]
