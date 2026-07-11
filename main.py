from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def dados_aluno():
    return {
        "matricula": "2024118isinf0076",
        "nome": "Jéssica França"
    }
