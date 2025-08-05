# Configuration des Groups et Permissions

## Permissions personnalisées sur le modèle Book

| Codename      | Description                |
|---------------|----------------------------|
| bookshelf.can_view   | Peut voir les livres     |
| bookshelf.can_create | Peut créer des livres    |
| bookshelf.can_edit   | Peut modifier des livres |
| bookshelf.can_delete | Peut supprimer des livres|

## Groupes

- **Viewers**  
  - Permissions : `bookshelf.can_view`

- **Editors**  
  - Permissions : `bookshelf.can_view`, `bookshelf.can_create`, `bookshelf.can_edit`

- **Admins**  
  - Permissions : toutes les permissions sur `Book` (création, modification, suppression, vue)

## Assignation

1. Dans l’admin Django, créez ces 3 groupes.
2. Assignez les permissions listées à chaque groupe.
3. Ajoutez des utilisateurs aux groupes selon leur rôle.
