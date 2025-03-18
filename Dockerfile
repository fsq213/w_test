FROM python:3.9
EXPOSE 8501
WORKDIR /app/123
COPY . .
RUN sudo apt-get update && sudo apt-get install python3-distutils && pip install -r requirements.txt 

CMD streamlit run app.py \
    --server.headless true \
    --browser.serverAddress="0.0.0.0" \
    --server.enableCORS false \
    --browser.gatherUsageStats false
