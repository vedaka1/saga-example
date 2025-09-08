# Installation
## Docker-compose
Create `.env` and `.env.production` from `.env.example` template

```bash
docker compose -f ../docker-compose.yaml up -d
```
- Swagger: `http://localhost:8000/docs`
- Mongo Express: `http://localhost:8081` (admin, admin)
- MongoDB: `mongodb://localhost:27017`
