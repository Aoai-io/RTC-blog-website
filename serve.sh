#!/bin/bash

echo $(cd /home/osama/)
echo $(source /venv/bin/activate)
echo $(pwd)
echo $(cd /home/osama/RTC-blog-website && touch tmp.deploy.txt)
# echo $(touch /home/osama/RTC-blog-website/tmp.deploy.txt)
echo $(git pull origin main)
echo $(date)
echo $(pwd)

echo $(pip install -r requirements.txt)
echo $(python manage.py migrate)
echo $(echo Omar@wolf.9803 | sudo -S systemctl restart gunicorn.service)
echo $(echo Omar@wolf.9803 | sudo -S systemctl restart nginx.service)
echo $(cp /home/osama/RTC-blog-website/tmp.deploy.txt /home/osama/logs/deploy.txt)
echo $(rm tmp.deploy.txt)
