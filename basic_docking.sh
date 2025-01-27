#!/bin/bash

# Arrêter le script en cas d'erreur
set -e

# Préparation du récepteur
# Génère le fichier PDBQT du récepteur avec les hydrogènes polaires et les charges partielles
# Crée également un fichier TXT et un fichier PDB définissant les dimensions de la boîte de docking
conda run -n meeko_env mk_prepare_receptor.py -i ./datas/1iep_receptorH.pdb -o 1iep_receptor -p -v \
    --box_size 20 20 20 --box_center 15.190 53.903 16.917;

# Préparation du ligand
# Ajoute les hydrogènes manquants au ligand et génère le fichier PDBQT correspondant
conda run -n meeko_env mk_prepare_ligand.py -i ./datas/1iep_ligand.sdf -o 1iep_ligand.pdbqt;

# Exécution du docking avec AutoDock Vina
# Utilise le fichier de configuration généré lors de la préparation du récepteur
conda run -n vina_env python3 launch_vina.py --sf_name vina --receptor ./1iep_receptor.pdbqt --ligand ./1iep_ligand.pdbqt \
    --box ./1iep_receptor.box.txt --exhaustiveness=32 --output ./1iep_ligand_vina_out.pdbqt;
