from fastapi import FastAPI

app = FastAPI(title="Loja de Itens")

# Armazenamento em memória: {id: item}
items = {}
next_id = 1
