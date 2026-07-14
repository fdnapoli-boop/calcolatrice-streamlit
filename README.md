# Calcolatrice con Streamlit

Una piccola web-app che riceve due numeri ed esegue somma, sottrazione,
moltiplicazione o divisione. La divisione per zero viene intercettata e mostrata
all'utente come messaggio di errore.

## Avvio sul computer

Richiede Python 3.10 o successivo. Da PowerShell, nella cartella del progetto:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt
python -m streamlit run app.py
```

Per interrompere l'app, premi `Ctrl+C` nel terminale.

## Test

```powershell
python -m pytest
```

## Pubblicazione su Streamlit Community Cloud

1. Crea un account gratuito su GitHub, se non ne possiedi uno.
2. Crea su GitHub un nuovo repository, per esempio `calcolatrice-streamlit`.
3. Carica nel repository tutti i file di questa cartella, mantenendo invariata
   la struttura. `app.py` e `requirements.txt` devono essere nella radice.
4. Accedi a <https://share.streamlit.io> e collega il tuo account GitHub.
5. Nel tuo workspace seleziona **Create app** e poi **Yup, I have an app**.
6. Seleziona il repository, il branch `main` e indica `app.py` come file principale.
7. Facoltativamente scegli un indirizzo nel campo **App URL**. Per questa app non
   servono secret né impostazioni avanzate.
8. Premi **Deploy**. Dopo la preparazione comparirà un indirizzo pubblico con
   dominio `streamlit.app`, che potrai condividere.

I successivi aggiornamenti inviati al repository GitHub vengono rilevati e
pubblicati automaticamente da Community Cloud.

## Struttura

```text
streamlit-task-app/
├── app.py                  # Interfaccia web
├── task_app/
│   ├── __init__.py         # Esportazioni del pacchetto
│   └── calculator.py       # Operazioni matematiche
├── tests/
│   └── test_calculator.py  # Test della calcolatrice
├── .gitignore
├── README.md
├── requirements.txt        # Dipendenze dell'app online
└── requirements-dev.txt    # Dipendenze locali e di test
```
