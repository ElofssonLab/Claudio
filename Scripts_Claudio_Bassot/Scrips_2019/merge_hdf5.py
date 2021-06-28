import h5py
import numpy as np
import os

d_names = os.listdir(os.getcwd())


# function to return a list of paths to each dataset
def getdatasets(key,archive):

  if key[-1] != '/': key += '/'

  out = []

  for name in archive[key]:

    path = key + name

    if isinstance(archive[path], h5py.Dataset):
      out += [path]
    else:
       out += getdatasets(path,archive)

  return out


# open HDF5-files
for g in d_names:
    data     = h5py.File(g,'r')
    new_data = h5py.File('new.hdf5','a')

# read as much datasets as possible from the old HDF5-file
    datasets = getdatasets('/',data)
  #  datasets = getdatasets('/',data)
# get the group-names from the lists of datasets
 #   groups = d_names
   # groups = [i for i in groups if len(i)>0]

# sort groups based on depth
    #idx    = np.argsort(np.array([len(i.split('/')) for i in groups]))
    #groups = [groups[i] for i in idx]

# create all groups that contain dataset that will be copied
for g in d_names:
    print g
    new_data.create_group(g)
    data.copy(data, new_data[g])
# copy datasets
 #   for path in datasets:
 #       print path
  # - get group name
  #      group = path[::-1].split('/',1)[1][::-1]

  # - minimum group name
   #     if len(group) == 0: group = '/'

  # - copy data
#        print d
 #       data.copy(g, new_data[d])
