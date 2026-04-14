FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -e .

CMD ["dotflow", "start", "--workflow", "{{MODULE_NAME}}.workflow:main", "--mode", "{{EXECUTION_MODE}}"]
