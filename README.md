# memory-chartline
# show memory in linechart
# datetime base of celery
# run project
1-python3 manage.py runserver
2-celery -A celeryProj worker -l info
3-celery -A persion beat -l info 
