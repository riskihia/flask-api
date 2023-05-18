# CONTRIBUTIING

## How to run Dockerfile localy

```
docker run -dp 5000:5000 -w /app -v "$(pwd):/app" image-name sh -c "flask run"
```