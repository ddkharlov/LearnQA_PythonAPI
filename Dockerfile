FROM python
WORKDIR /python-api-learn/
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV ENV=dev
CMD python -m pytest -s --alluredir=test_results/ /python-api-learn/tests/