cd app/rasa/
# Start rasa server with nlu model
rasa run --credentials ./credentials.yml  --enable-api --auth-token XYZ123 --model ./models --endpoints ./endpoints.yml --enable-api --cors "*" --debug \
         -p $PORT
rasa run actions