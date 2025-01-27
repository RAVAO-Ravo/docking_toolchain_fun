#!/bin/bash
#-*- coding:utf-8 -*-

# Dossier contenant les fichiers .yml
YML_DIR="./envs"

# Vérifier si le dossier existe
if [ ! -d "$YML_DIR" ]; then
    echo "Le dossier $YML_DIR n'existe pas. Veuillez vérifier le chemin."
    exit 1
fi

# Parcourir tous les fichiers .yml dans le dossier
for yml_file in "$YML_DIR"/*.yml; do
    if [ -f "$yml_file" ]; then
        # Extraire le nom de l'environnement à partir du fichier yml
        env_name=$(grep -m 1 '^name:' "$yml_file" | awk '{print $2}')
        
        if [ -n "$env_name" ]; then
            echo "Suppression de l'environnement Conda : $env_name"
            
            # Supprimer l'environnement Conda
            conda env remove -n "$env_name"
            
            # Vérifier si la suppression a réussi
            if [ $? -eq 0 ]; then
                echo "Environnement $env_name supprimé avec succès."
            else
                echo "Échec de la suppression de l'environnement $env_name."
            fi
        else
            echo "Impossible de trouver le nom de l'environnement dans $yml_file."
        fi
    else
        echo "Aucun fichier .yml trouvé dans le dossier $YML_DIR."
    fi
done
