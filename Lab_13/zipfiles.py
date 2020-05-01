import zipfile

z = zipfile.ZipFile('test.zip', 'r')
z.namelist()  # parcurge inclusiv directoarele si da pathurile complet, a fisierelor din arhiva intr-o lista
z.infolist()  # intoarce pt fiecare director si fisier din arhiva un obiect ZipInfo
# ZipInfo are o metoda isdir, au filename - da pathul relativ la arhiva, compress
z.getinfo('test.txt')  # primeste ca param un path din interiorul arhivei si intoarce un ZipInfo
z.extractall()  # despacheteaza toata arhiva, daca nu dam parametrul pt unde il despacheteaza, va fi directorul curent
z.extract(
    'test.txt')  # primeste numele unui membru si il despacheteaza doar pe acela + parametru pt unde sa-l despacheteze

# Ca sa scriem intr-o arhiva , deschidem cu 'w'
z.write('k.txt', 'd/')  # primeste un path de pe disk
