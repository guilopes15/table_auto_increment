
### Comando para subir o server
```bash
poetry run fastapi dev src/table_auto_increment/app.py --host 0.0.0.0 --reload
```
### Comando para iniciar a automação
```bash
poetry run python -m src.table_auto_increment.selenium
_automation.main
```