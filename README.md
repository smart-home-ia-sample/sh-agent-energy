# sh-agent-energy

Energy A2A agent: `inspect_consumption` and `identify_critical_devices`.

Part of the **Smart Home AI** system — architecture, the full `docker compose`
stack and the end-to-end tests live in `sh-infra`.

## Run the tests
```
pip install -r requirements-dev.txt   # needs sh-common from the registry
pytest
```

## Build the image
```
docker build -t sh-agent-energy .
```
