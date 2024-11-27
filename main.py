from fastapi import FastAPI, HTTPException
from typing import List

app = FastAPI()


class Produkt:
    def __init__(self, id: int, nazwa: str, cena: float):
        self.id = id
        self.nazwa = nazwa
        self.cena = cena

    def get_info(self) -> str:
        return f"Produkt {self.nazwa}, Cena: {self.cena} PLN"

    def apply_discount(self, procent: float) -> None:
        self.cena -= self.cena * (procent / 100)

class Kategoria:
    def __init__(self, id: int, nazwa: str):
        self.id = id
        self.nazwa = nazwa
        self.produkty: List[Produkt] = []

    def dodaj_produkt(self, produkt: Produkt) -> None:
        self.produkty.append(produkt)

    def usun_produkt(self, produkt_id: int) -> None:
        self.produkty = [p for p in self.produkty if p.id != produkt_id]

produkty_db: List[Produkt] = []
kategorie_db: List[Kategoria] = []

@app.post("/produkty/")
def dodaj_produkt(id: int, nazwa: str, cena: float):
    for produkt in produkty_db:
        if produkt.id == id:
            raise HTTPException(status_code=400, detail="Produkt o tym ID już istnieje.")
    nowy_produkt = Produkt(id, nazwa, cena)
    produkty_db.append(nowy_produkt)
    return {"message": "Produkt dodany pomyślnie."}

@app.get("/produkty/{produkt_id}")
def pobierz_produkt(produkt_id: int):
    for produkt in produkty_db:
        if produkt.id == produkt_id:
            return {
                "id": produkt.id,
                "nazwa": produkt.nazwa,
                "cena": produkt.cena
            }
    raise HTTPException(status_code=404, detail="Produkt nie znaleziony.")

@app.put("/produkty/{produkt_id}")
def aktualizuj_produkt(produkt_id: int, nazwa: str = None, cena: float = None):
    for produkt in produkty_db:
        if produkt.id == produkt_id:
            if nazwa is not None:
                produkt.nazwa = nazwa
            if cena is not None:
                produkt.cena = cena
            return {"message": "Produkt zaktualizowany pomyślnie."}
    raise HTTPException(status_code=404, detail="Produkt nie znaleziony.")

@app.delete("/produkty/{produkt_id}")
def usun_produkt(produkt_id: int):
    global produkty_db
    produkty_db = [p for p in produkty_db if p.id != produkt_id]
    return {"message": "Produkt usunięty pomyślnie."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
