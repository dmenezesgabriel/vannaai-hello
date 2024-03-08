# Vanna Ai Local

## Usage

- **Run services**:

```sh
docker compose up
```

- **Access ollama shell**:

```sh
docker compose exec -it ollama-llm /bin/sh
```

- **Pull LLM model**:

```sh
ollama pull mistral
```

- **Run LLM model**:

```sh
ollama run mistral
```

## Resources

- [vanna.ai](https://vanna.ai/docs/sqlite-ollama-chromadb/)
- [medium](https://medium.com/@pbvillaflores/running-vanna-local-on-python-38d72afb06ad)
