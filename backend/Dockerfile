FROM python:3.11

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY app.py /app/
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["python", "app.py"]