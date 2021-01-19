up:
	uvicorn 'api.main:app' --workers 1 --host 0.0.0.0 --http h11 --reload
