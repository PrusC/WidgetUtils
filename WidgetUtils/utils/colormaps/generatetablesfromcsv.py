from os import path, listdir


dirname = r'./CETperceptual_csv_0_255'
pathname = path.join(path.dirname(__file__), dirname)
files = listdir(pathname)


# res = open('./utils/seismic_data.py', 'a')
res = open('cet_tables.py', 'w')
res.write(r"# colormaps from https://colorcet.com")
res.write('\n')

for filename in files:
    name = filename.split('.')[0]
    if name.find('-'):
        name = name.replace('-', '_')
    res.write('\n\n')
    res.write(name + ' = [\\\n')
    with open(dirname + '\\' + filename) as file:
        for f in file:
            res.write('[')
            res.write(', '.join(f.strip('\n').split(',')))
            res.write('],\n')
    res.write(']\n')



