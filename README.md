# DemoCorsoGithubCopilotPython

## Gioca a tris nel browser

Installa le dipendenze in un ambiente virtuale:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Avvia il server web:

```powershell
python app.py
```

Apri <http://127.0.0.1:5000> nel browser. Due giocatori si alternano
scegliendo una casella da 1 a 9; il primo gioca con `X` e il secondo con `O`.
Il pulsante **Nuova partita** azzera la partita corrente.

## Gioco da terminale

Il gioco originale resta disponibile:

```powershell
python tic_tac_toe.py
```

## Test

Esegui tutti i test:

```powershell
python -m unittest -v
```

Esegui un singolo test web:

```powershell
python -m unittest -v test_app.WebAppTests.test_moves_are_played_and_winner_is_shown
```