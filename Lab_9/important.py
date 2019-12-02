import os

for root, dirs, files in os.walk('.'):
    print('It 1 ===================')
    print(root)
    print(os.path.abspath(
        root))  # echivalent cu join intre current working directory adica .-ul, rootul proiectului adica
    # si root

    for x in dirs + files:
        print()
        print('It 2')
        print(x)
        print(os.path.abspath(
            x))  # concatenarea relativ la current working directory care nu s-a schimbat. va fi d:/projects/x, /y, /z
        fp = os.path.join(root, x)  # ca sa dea corect pathul complet
        print(fp)
