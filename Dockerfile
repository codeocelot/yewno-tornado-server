FROM python:2-onbuild
ADD . /code
WORKDIR /code
CMD [ "python", "/code/server.py" ]
EXPOSE 3000
