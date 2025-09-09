# Run project
## Docker-compose
You can also pass container name with `cont=<container_name>` argument where its possible
- ### Run project (supports `cont=`)
    ```bash
    make dev
    ```
- ### Run tests
    ```bash
    make tests
    ```
- ### Shutdown project
    ```bash
    make down
    ```
- ### View last 500 logs (supports `cont=`)
    ```bash
    make logs
    ```
- ### Restart (supports `cont=`)
    ```bash
    make restart
    ```
## Links:
### user-service
- Mongo - `mongodb://mongodb:27017`
- Mongo Express - http://localhost:8081 (admin, admin)
- Swagger - http://localhost:8000/docs
