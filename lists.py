# Create lists for iteration

list_str = ['01','02','03','04']#,'05','06','07','08','09'] + list(map(str, range(10, 31)))

list_datafiles_raw_SIT = 'data/ecg_raw/SIT/ecg_{list_str}'
list_datafiles_raw_GAZE = 'data/ecg_raw/GAZE/ecg_{list_str}'

append_type = '.npy'
append_google = 'drive/MyDrive/Masterarbeit/Code/two-hearts/'

datafiles_raw_SIT = []
for i in range(len(list_str)):
    datafiles_str = list_datafiles_raw_SIT.format(list_str = list_str[i])
    datafiles_raw_SIT.append(datafiles_str)
datafiles_raw_SIT = [sub + append_type for sub in datafiles_raw_SIT]

datafiles_raw_GAZE = []
for i in range(len(list_str)):
    datafiles_str = list_datafiles_raw_GAZE.format(list_str = list_str[i])
    datafiles_raw_GAZE.append(datafiles_str)
datafiles_raw_GAZE = [sub + append_type for sub in datafiles_raw_GAZE]	


datafiles_raw_SIT_google = [append_google + sub for sub in datafiles_raw_SIT]
datafiles_raw_GAZE_google = [append_google + sub for sub in datafiles_raw_GAZE]

