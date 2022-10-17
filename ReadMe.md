# ReadMe

Le code est divisé en plusieurs librairies, chacune dans son dossier

## memory

C'est dans ce dossier que vont se situer les fichiers, les classes et les exceptions relatifs à tout ce qui est stockage des données, voire même définition d'interfaces vers des db distantes, des factories, etc...

## pathsMethods

Dans ce dossier vont se situer les fichiers (...) relatifs aux fonctions que le serveur api applique lorsqu'il reçoit une requête. Ces fonctions sont déportées du main pour conserver une certaine lisibilité



> Vous trouverez dans l'entête de nombreux fichiers les lignes suivantes:
> 
> ```python
> LOCAL_DIRECTORY = os.getcwd()
> sys.path.append(os.path.join(LOCAL_DIRECTORY, "memory"))
> sys.path.append(os.path.join(LOCAL_DIRECTORY, "pathsMethods"))
> ```
> 
> LOCAL_DIRECTORY aura toujours la valeur du path du dossier parent du script python appelé par la console.
> 
> les lignes suivantes visent à obtenir les paths des fichiers situés dans les librairies. Cette syntaxe est nécessaire car nous ne programmons pas tous sous le même os, les paths ne sont pas écrits de la même façon

> A noter que un fichier donné ne trouvera les libraires avec cette écriture seulement si ce fichier n'est pas exécuté directement, il doit être appelé par le main. Si vous souhaitez tester votre code, modifier ces lignes pour le test