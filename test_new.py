import os
import shutil
from os.path import join

sourcepath_in='/home/jam/Test_Folder/IN'
sourcefiles_in = os.listdir(sourcepath_in)


sourcepath_out_bus='/home/jam/Test_Folder/OUT_BUS'
sourcefiles_out_bus = os.listdir(sourcepath_out_bus)
sourcepath_out_nco='/home/jam/Test_Folder/OUT_BUS'
sourcefiles_out_nco = os.listdir(sourcepath_out_nco)
sourcepath_out_bo='/home/jam/Test_Folder/OUT_BO'
sourcefiles_out_bo = os.listdir(sourcepath_out_bo)

sourcepath_out_test='/home/jam/Test_Folder/OUT_TEST'
sourcefiles_out_test = os.listdir(sourcepath_out_test)


destinationpath_in_bus = '/home/jam/Test_Folder/IN_BUS'
destinationpath_in_nco = '/home/jam/Test_Folder/IN_NCO'
destinationpath_in_bo = '/home/jam/Test_Folder/IN_BO'
destinationpath_in_out = '/home/jam/Test_Folder/OUT'
destinationpath_in_test = '/home/jam/Test_Folder/IN_TEST'


suffixes_in_nco = ("Airi", "Reci", "Rcmi", "Siri", "Srai", "Srmi", "Ladi", "Lidi", "Lcdi", "Lmdi", "Lami", "Limi", "Tncc", "Rcmc", "Recc", "Oirc", "Srmc", "Srac", "Blni", "In1i", "In2i", "Gufi", "Pnli", "R02i", "R03i", "Riai", "Acti", "Dsri", "Rmri")
suffixes_in_bo = ("Erri", "Reji", "Trei", "Tnci", "Bavi", "Bini", "Dcti", "Mbri", "Crri", "Crfi", "Mafi", "Mfri", "Slai", "Trec", "Errc", "Rejc", "Crti", "Slci", "Slri", "Crli", "Stpi")
suffixes_in_bus = ("Oiri", "Frif", "Fris", "Frof", "Fros", "Fidr", "Fiwr", "Fimr", "Fiqr", "Fadr", "Fawr", "Famr", "Faqr")

suffixes_test=("_T_")
suffixes_prod=("_P_")


for file in sourcefiles_in:
    start_suffixes = 0
    check_t = 0
    if file.count( "_", 0 , 12) == 2:
        start_suffixes = 10
        test_check = 14
    elif file.count( "_", 0 , 12) == 3:
        start_suffixes = 5
        test_check = 9 

    if file.startswith(suffixes_test, test_check):
        shutil.move(os.path.join(sourcepath_in,file), os.path.join(destinationpath_in_test,file)) 
    elif file.startswith(suffixes_prod, test_check):
        if file.startswith(suffixes_in_nco, start_suffixes):
            shutil.copy(os.path.join(sourcepath_in,file), os.path.join(destinationpath_in_bus,file))
            shutil.move(os.path.join(sourcepath_in,file), os.path.join(destinationpath_in_nco,file))
        elif file.startswith(suffixes_in_bo, start_suffixes):
            shutil.move(os.path.join(sourcepath_in,file), os.path.join(destinationpath_in_bo,file))
        elif file.startswith(suffixes_in_bus, start_suffixes):
            shutil.move(os.path.join(sourcepath_in,file), os.path.join(destinationpath_in_bus,file))
        else :
            shutil.copy(os.path.join(sourcepath_in,file), os.path.join(destinationpath_in_bus,file))
            shutil.copy(os.path.join(sourcepath_in,file), os.path.join(destinationpath_in_bo,file))
            shutil.move(os.path.join(sourcepath_in,file), os.path.join(destinationpath_in_nco,file))

for file in sourcefiles_out_test:
    start_suffixes = 0
    check_t = 0
    if file.count( "_", 0 , 12) == 2:
        start_suffixes = 10
        test_check = 14
    elif file.count( "_", 0 , 12) == 3:
        start_suffixes = 5
        test_check = 9

    if file.startswith(suffixes_test, test_check):
        shutil.move(os.path.join(sourcepath_out_test,file), os.path.join(destinationpath_out,file))


for file in sourcefiles_out_bus:
    start_suffixes = 0
    check_t = 0
    if file.count( "_", 0 , 12) == 2:
        start_suffixes = 10
        test_check = 14
    elif file.count( "_", 0 , 12) == 3:
        start_suffixes = 5
        test_check = 9

    if file.startswith(suffixes_prod, test_check):
        shutil.move(os.path.join(sourcepath_out_bus,file), os.path.join(destinationpath_out,file))

for file in sourcefiles_out_bo:
    start_suffixes = 0
    check_t = 0
    if file.count( "_", 0 , 12) == 2:
        start_suffixes = 10
        test_check = 14
    elif file.count( "_", 0 , 12) == 3:
        start_suffixes = 5
        test_check = 9

    if file.startswith(suffixes_prod, test_check):
        shutil.move(os.path.join(sourcepath_out_bo,file), os.path.join(destinationpath_out,file))

for file in sourcefiles_out_nco:
    start_suffixes = 0
    check_t = 0
    if file.count( "_", 0 , 12) == 2:
        start_suffixes = 10
        test_check = 14
    elif file.count( "_", 0 , 12) == 3:
        start_suffixes = 5
        test_check = 9

    if file.startswith(suffixes_prod, test_check):
        shutil.move(os.path.join(sourcepath_out_nco,file), os.path.join(destinationpath_out,file))
