from		python:3.7-alpine
workdir		/code
ENV		FLASK_APP=app.py
ENV		FLASK_RUN_HOST=0.0.0.0
run		apk add --no-cache gcc musl-dev linux-headers
copy		requirments.txt requirments.txt
run		pip install -r requirments.txt
copy		app.py app.py
expose		5000
cmd		["flask", "run"]
