FROM python:2.7.14-stretch
ADD . /stringer
WORKDIR /stringer
RUN pip install -r requirements.txt
CMD ["python", "permutations.py"]