FROM public.ecr.aws/lambda/python:3.8

RUN mkdir -p /app
COPY . /app/
WORKDIR /app
RUN pip install -r requirements.txt
CMD [ "first_n_squares.py" ]
ENTRYPOINT [ "python" ]