<<<<<<< HEAD
cd app/
=======
cd /app
>>>>>>> 25d7e558e0b50f65fa15bfaea01d0348b3d91d39
rasa train && rasa run --credentials ./credentials.yml  --enable-api --auth-token XYZ123 --model ./models --endpoints ./endpoints.yml --enable-api --cors "*" --debug \ -p $PORT
