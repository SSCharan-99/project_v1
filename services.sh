cd app/
# Start rasa server with nlu model
rasa train && rasa run --credentials ./credentials.yml  --enable-api --auth-token XYZ123 --model ./models --endpoints ./endpoints.yml --enable-api --cors "*" --debug \ -p $PORT
