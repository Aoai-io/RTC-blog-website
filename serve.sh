#!/bin/bsh

echo $(date)
echo $(cd /home/osama/RTC-blog-website)
echo $(source ../venv/bin/activate)

echo $(pip install -r requirements.txt)
echo $(python manage.py migrate)
echo $(Omar@wolf.9803 | sudo -S systemctl restart gunicorn.service)
echo $(Omar@wolf.9803 | sudo -S systemctl restart nginx.service)
echo $(cp /home/osama/RTC-blog-website/tmp.deploy.txt /home/osama/logs/deploy.txt)
echo $(rm tmp.deploy.txt)
