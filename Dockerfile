FROM python:3.13
EXPOSE 8080
WORKDIR /ledgr-v1
COPY . ./
RUN pip install -r requirements.txt
ENTRYPOINT ["streamlit", "run", "Home.py", "--server.port=8080", "--server.address=0.0.0.0"]
