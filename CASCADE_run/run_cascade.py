import os 
import sys

def main():

    # change this to the CASCADE package path on your machine
    CASCADE_path = '/Users/benji/CASCADE_package/CASCADE' 

    sys.path.insert(0, CASCADE_path)
    from CASCADE import prediction

    save_folder = os.getcwd()
    path_csv = save_folder + '/CASCADE_inputs.csv'
    prediction(save_folder, path_csv)

if __name__ == '__main__':
    main()

