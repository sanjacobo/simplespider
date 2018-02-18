sudo python setup.py bdist_egg

curl http://localhost:6800/addversion.json -F project=spidertest -F version=r23 -F egg=@spidertest-0.1-py2.7.egg

curl http://localhost:6800/schedule.json -d project=spidertest -d spider=quotes

sudo pip install scrapy

sudo pip install scrapyd
