# Métaclasse de vérification de type en Python

## Description

Ce projet contient une métaclasse Python, `CheckTypesMeta`, qui applique un décorateur de vérification de type à toutes les méthodes d'une classe. Le décorateur vérifie si les types des arguments passés à une fonction correspondent aux annotations de type de cette fonction. Si ce n'est pas le cas, il lève une exception `TypeError`. Il vérifie également si les arguments possêdent bien un type. Si ce n'est pas le cas, il lève une exception `TypeError`.

## Installation

Pour installer ce projet, vous devez cloner ce dépôt sur votre machine locale. Vous pouvez le faire en utilisant la commande suivante :

```bash
git clone https://github.com/maximegg/CheckTypes_python.git
```

## Utilisation

Pour utiliser cette métaclasse, vous devez d'abord l'importer dans votre fichier Python :

```python
from checktypes import CheckTypesMeta
```

Ensuite, vous pouvez définir `CheckTypesMeta` comme métaclasse de votre classe :

```python
class MaClasse(metaclass=CheckTypesMeta):
    def ma_methode(self, arg1: int, arg2: str):
        pass
```

Maintenant, si vous essayez d'appeler `ma_methode` avec des arguments qui ne correspondent pas aux annotations de type, une exception `TypeError` sera levée.

## Contribution

Les contributions à ce projet sont les bienvenues. Si vous souhaitez contribuer, veuillez forker le dépôt, apporter vos modifications et soumettre une pull request.

## Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE`
