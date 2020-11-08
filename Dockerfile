FROM python:3

ADD src /src

CMD [ "python", "./Tests/CalculatorTest.py" ]