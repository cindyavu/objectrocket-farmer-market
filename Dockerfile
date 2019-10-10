FROM python:3.7
WORKDIR /app/
COPY Main.py .
COPY Product.py .
COPY Promo.py .
COPY Store.py .
COPY test_Store.py .
COPY Product_List.txt .
COPY Promos.txt .
COPY requirements.txt . 
COPY run_clients.sh .

RUN pip install -r requirements.txt

CMD [ "sh", "run_clients.sh"]


