import pickle
from lag_pickle import Kunde

FILENAME_PICK='Kunde.dat'

def main():
    end_of_file = False
    alle_kunder=[]
    # Open the file.
    input_file = open(FILENAME_PICK, 'rb')
    # Read to the end of the file.
    while not end_of_file:
        try:
            # Unpickle the next object.
            kunde = pickle.load(input_file)
            #legg til i liste
            alle_kunder+=[kunde]
        except EOFError:
            # Set the flag to indicate the end
            # of the file has been reached.
            end_of_file = True
    # Close the file.
    input_file.close()

    for kunde in alle_kunder:
        print()
        print('Mobilnr:\t',kunde.get_mobilnr())
        print('Etternavn:\t',kunde.get_etternavn())
        print('Mobilnr:\t',kunde.get_epost())
main()