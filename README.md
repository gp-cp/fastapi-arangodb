# fastapi-arangodb

Try out fastapi with arangodb.


## Install with poetry

```
poetry install
```
## Start arangodb
```
docker-compose up -d
```

## Start the app
```
hypercorn app.main:server
```