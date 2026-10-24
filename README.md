# sqlite-constraint-replay

## Français

Observer quand une transaction viole réellement ses clés étrangères.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m sqlite_constraint_replay examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Exécute une transaction SQLite réelle avec clés étrangères immédiates ou différées ; sépare acceptation d’une instruction et validation du commit, puis relit la base après rollback.

### Limites

Deux tables de référence et opérations insert/delete seulement. Pas de migration en production, de concurrence multiconnexion ni de validation d’un autre moteur.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Observe when a transaction actually violates its foreign keys.

Synthetic data; no network access or secret required.

```sh
python -m sqlite_constraint_replay examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Executes an actual SQLite transaction with immediate or deferred foreign keys; separates statement acceptance from commit validation, then reads state after rollback.

### Limits

Two reference tables and insert/delete only. No production migration, multi-connection concurrency or validation of another database engine.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Observar cuándo una transacción viola realmente sus claves foráneas.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m sqlite_constraint_replay examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Ejecuta una transacción SQLite real con claves foráneas inmediatas o diferidas; separa aceptación de sentencia y validación del commit, y relee estado tras rollback.

### Límites

Dos tablas de referencia y solo insert/delete. Sin migración en producción, concurrencia multiconexión ni validación de otro motor.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.sqlite.org/foreignkeys.html
