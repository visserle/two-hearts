# Create lists for iteration

list_str = ['01','02','03','04','05','06','07','08','09'] + list(map(str, range(10, 70)))

list_datafiles_raw = 'sample-data/raw/00{list_str}'
list_datafiles_1k = 'sample-data/1k/00{list_str}'
list_datafiles = 'sample-data/00{list_str}'

append_type = '.npy'
append_google = 'drive/MyDrive/Masterarbeit/Code/two-hearts/'

datafiles_wfdb = []
for i in range(len(list_str)):
    datafiles_str = list_datafiles_raw.format(list_str = list_str[i])
    datafiles_wfdb.append(datafiles_str)

datafiles_raw = []
for i in range(len(list_str)):
    datafiles_str = list_datafiles_raw.format(list_str = list_str[i])
    datafiles_raw.append(datafiles_str)
datafiles_raw = [sub + append_type for sub in datafiles_raw]

datafiles_1k = []
for i in range(len(list_str)):
    datafiles_str = list_datafiles_1k.format(list_str = list_str[i])
    datafiles_1k.append(datafiles_str)
datafiles_1k = [sub + append_type for sub in datafiles_1k]

datafiles = []
for i in range(len(list_str)):
    datafiles_str = list_datafiles.format(list_str = list_str[i])
    datafiles.append(datafiles_str)
datafiles = [sub + append_type for sub in datafiles]

datafiles_raw_google = [append_google + sub for sub in datafiles_raw]
datafiles_google = [append_google + sub for sub in datafiles]
