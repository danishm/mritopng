FROM python:onbuild
RUN pip install nose
RUN python setup.py install
RUN nosetests -v
RUN mritopng