import os


# Function to rename multiple files
def main():
    for count, filename in enumerate(os.listdir("data\cboundry")):
        dst = str(count) + ".jpg"
        src = 'data/cboundry/' + filename
        dst = 'data/cboundry/' + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)

    # Driver Code


if __name__ == '__main__':
    # Calling main() function
    main()
# import os
# folderpath=r'F:\sgp_5sem\data\cboundry'
# filenum=500
#
# for filename  in os.listdir(folderpath):
#     os.rename(folderpath+'\\'+filename,folderpath+'\\'+filename+'.jpg')
#     filenum++1
