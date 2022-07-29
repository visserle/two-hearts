# two-hearts
Investigating Physiological Synchrony via Deep Learning.

Voraussetzungen:
- Conda-Umgebung unter requirements.txt

Python-Skripts:
- functions -> Funktionen zur trigonometischen Interpolation
- lists -> Anzahl der Versuchsteilnehmer

Jupyter Notebooks:
- 00_acq -> Zuschneiden der experimentellen EKG-Daten. Benötigt zusätzlich bioread package.
- 01_preprocessing -> Aufbereitung der EKG-Daten
- 02_model -> Deep Learning
- 02_model_plots -> Explorative Analyse des Deep Learnings
- 03_heartrates -> Analyse auf Makroebene
- 04_more_plots -> Visualisierungen der Zeitreihen
- 05_simulation -> Deep Learning mit simulierten Daten

Daten:
- data/ -> Datengrundlage für das Deep Learning
- data/ecg_raw -> experimentelle EKG-Daten und zugeschnittene Daten
- model/ -> Deep Learning Modelle (data_all.pickle als nested dictionary mit allen Daten aus 02_model)
- plots/ -> Visualisierungen
