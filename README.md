# docking_toolchain_fun

Ce projet vise à simplifier et automatiser l'installation et l'utilisation d'outils nécessaires pour effectuer du docking moléculaire avec AutoDock Vina. Grâce à des environnements Conda dédiés, chaque outil est isolé pour éviter les conflits de dépendances.

Un script (`basic_docking.sh`) permet de vérifier que l'installation et la configuration des outils sont correctes, en exécutant un exemple de docking de base.

## Prérequis

Avant de commencer, assurez-vous d'avoir **Miniconda** installé sur votre machine. Vous pouvez télécharger Miniconda pour votre système d'exploitation depuis le site officiel : [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

## Instructions d'installation

1. Clonez ce dépôt :

   ```bash
    git clone https://github.com/RAVAO-Ravo/docking_toolchain_fun
    cd docking_toolchain_fun/
   ```

2. Installez les environnements Conda requis :

   ```bash
    bash installation_envs.sh
   ```

## Structure du Projet

1. **Scripts principaux :**

   - `basic_docking.sh` : Automatisation du tutoriel de base disponible sur [AutoDock Vina Documentation](https://autodock-vina.readthedocs.io/en/latest/docking_basic.html), vérifiant l'installation des outils, préparant les fichiers nécessaires (récepteur et ligand), et exécutant un docking.
   - `launch_vina.py` : Script Python pour l'exécution personnalisée des dockings avec configuration des paramètres.
   - `visualize.py` : Script Python pour la visualisation interactive de molécules.
   - `installation_envs.sh` : Automatisation de l'installation des environnements Conda à partir des fichiers YAML fournis.
   - `uninstallation_envs.sh` : Automatisation de la suppression des environnements Conda.

2. **Environnements Conda :**

   Les fichiers YAML définissent des environnements spécifiques pour chaque outil utilisé dans le pipeline de docking :

   - `autogrid_env.yml` : Pour AutoGrid4.
   - `meeko_env.yml` : Pour la préparation des ligands avec Meeko.
   - `nglv_env.yml` : Pour des visualisations interactives avec NGLView dans un notebook.
   - `scrubber_env.yml` : Pour le nettoyage des structures moléculaires avec Scrubber.
   - `vina_env.yml` : Pour l'exécution de dockings avec AutoDock Vina.

3. **Dossiers :**

   - `./datas` : Contient les fichiers nécessaires comme les structures du récepteur et du ligand.
   - `./envs` : Contient les fichiers YAML pour la configuration des environnements Conda.

## Utilisation

### Préparation et Docking

Exécutez le script `basic_docking.sh` :

```bash
bash basic_docking.sh
```

Ce script :

- Prépare le récepteur et le ligand.
- Configure la boîte de docking.
- Exécute AutoDock Vina avec les paramètres définis.

### Commandes disponibles pour `launch_vina.py`

Le script `launch_vina.py` offre des options pour personnaliser vos simulations de docking :

- **--sf\_name** : Fonction de score à utiliser (`vina` par défaut, ou `ad4`).
- **--ligand** : Chemin vers le fichier ligand au format PDBQT (obligatoire).
- **--output** : Chemin pour sauvegarder les résultats du docking au format PDBQT (obligatoire).
- **--exhaustiveness** : Détermine l'exhaustivité de la recherche (valeur par défaut : 8).
- **--num\_poses** : Nombre de poses à tester et sauvegarder (par défaut : 20).
- **--box** : Chemin vers le fichier de configuration de la boîte (obligatoire pour le mode `vina`).
- **--receptor** : Chemin vers le fichier récepteur au format PDBQT (obligatoire pour le mode `vina`).
- **--maps\_prefix** : Préfixe pour les fichiers de cartes pré-calculées (obligatoire pour le mode `ad4`).

Exemple d'utilisation :

```bash
python3 launch_vina.py --sf_name vina --receptor chemin/vers/recepteur.pdbqt --ligand chemin/vers/ligand.pdbqt --box chemin/vers/box.txt --output chemin/vers/output.pdbqt --exhaustiveness 32 --num_poses 10
```

### Désinstallation des Environnements

Pour supprimer les environnements Conda, exécutez :

```bash
bash uninstallation_envs.sh
```

## Remarques

Pour utiliser un outil spécifique, deux méthodes sont disponibles :

1. **Activation de l'environnement :** Activez l'environnement correspondant et exécutez la commande nécessaire à l'intérieur.

   ```bash
    conda activate <nom_de_l_environnement>
    command
   ```

2. **Utilisation directe avec ************`conda run`************ :** Lancez la commande sans activer l'environnement, en utilisant :

   ```bash
   conda run -n <nom_de_l_environnement> command
   ```

Cela permet d'isoler l'exécution sans affecter l'environnement courant de votre terminal.

## Licence

Ce projet est sous licence Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0). Vous êtes libre de :

- Partager : copier et redistribuer le matériel sous quelque support que ce soit ou sous n'importe quel format.
- Adapter : remixer, transformer et créer à partir du matériel.

Selon les conditions suivantes :

- Attribution : Vous devez donner le crédit approprié, fournir un lien vers la licence et indiquer si des modifications ont été apportées. Vous devez le faire de la manière suggérée par l'auteur, mais pas d'une manière qui suggère qu'il vous soutient ou soutient votre utilisation du matériel.

- Utilisation non commerciale : Vous ne pouvez pas utiliser le matériel à des fins commerciales.

[![Logo CC BY-NC 4.0](https://licensebuttons.net/l/by-nc/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc/4.0/)

[En savoir plus sur la licence CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)
