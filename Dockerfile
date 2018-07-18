FROM python:2.7

WORKDIR /home

COPY . /home
RUN pip install numpy seaborn pandas scipy matplotlib mpld3 jinja2
RUN python -m pip install --user "git+https://github.com/javadba/mpld3@display_fix"

CMD python /home/main.py

EXPOSE 9000