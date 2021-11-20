# MST_image_processing_deduplication
Uses the MST image set and removes duplicates, blurry, and hard to identify images

## Steps ##
The input.csv file includes all images from sets 1-6 and c-f with lure ratings in one large csv file. First multiple students went thorugh the image sets and manually added the file names based on the images ("what does the image depict?").
Additionally notes were created for image pairs that were blurry, conceptually similar (i.e.: different types of lawn mowers), and hard to idenitfy images. 
The dups.py first identifies *any* notes in the input.csv file, removes them, and outputs the removed files into deleted_images.csv. After this removal of manually identified images,
the code does a second duplicate removal process where it checks the names of the images and removes any duplicates based on names with identifying which image was the duplicate of which other image in the same or different set. 
The dups.py code then creates another output with the deleted additional dupliates called deleted_images_round_2.txt. 

The counts.py script counts the number of image pairs left by Lure ratings. 
