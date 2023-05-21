import CustomTableCreation as ctc

filePath = ctc.FileLocator()

with open(filePath, 'r') as fp:
    for l_no, line in enumerate(fp):
        # search string
        if 'placeholdername' in line:
            print('string found in a file')
            print('Line Number:', l_no)
            print('Line:', line)
            # don't look for next lines
            break

def rewriteTableName(fp):
    print("placeholder in wtn")