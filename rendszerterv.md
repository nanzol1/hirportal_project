# Híroldal Rendszerterv

## 1. Felhasznált technológiák
- **Frontend**: Bootstrap (HTML, CSS, JavaScript)
- **Backend**: Flask (Python)
- **Adatbázis**: SQLite

## 2. Funkciók
- **Főoldal**: Hírlista cím, dátum és szerző alapján.
- **Hírnézet**: Egy adott hír teljes tartalmának megjelenítése.
- **Adminfelület**: Hírek létrehozása, szerkesztése, törlése.

## 3. Adatfolyam
- A **felhasználók** lekérik a híreket a Flask backendtől, amely SQL-lekérdezéseket hajt végre az SQLite-adatbázisból.
- Az **adminisztrátorok** a Flask adminisztrációs felületén keresztül kezelik a híreket.

## 4. Rendszerkommunikáció
- A Flask backend REST API-t használ az adatok kezelésére, míg a Bootstrap biztosítja a reszponzív megjelenítést.
