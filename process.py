from google_images_download import google_images_download
import os, errno
import time
from summary import summarize

# def silent_remove_of_file(file):
#     try:
#         os.remove(file)
#     except OSError as e:
#         if e.errno != errno.ENOENT:
#             raise e
#         return False
#     return True



'''
    We haven't considered the subtitle yet
'''
def download_images(keyword, i):
    start_time = time.time()
    arguments = {
        "keywords": keyword, # the keyword to search
        "limit": 5,
        "print_urls": False,
        "image_directory":str(i) # the directory to which images are downloaded under downloads/
        # "format":"jpgpng"
    }
    try:
        temp = arguments['output_folder']
    except KeyError:
        pass
    else:
        assert False, "This test checks download to default location yet an output folder was provided"

    output_folder_path = os.path.join(os.path.realpath('.'), 
                'downloads', 
                '{}'.format(i))
                # '{}'.format(argumnets['keywords']))
                # '{}'.format(argumnets['keywords']))
                
    # if os.path.exists(output_folder_path):
    #     start_amount_of_files_in_output_folder = len([name for name in os.listdir(output_folder_path) if os.path.isfile(os.path.join(output_folder_path, name)) and os.path.getctime(os.path.join(output_folder_path, name)) < start_time])
    # else:
    #     start_amount_of_files_in_output_folder = 0

    response = google_images_download.googleimagesdownload()
    response.download(arguments)
    # print("\n\n")
    # print(downloaded_paths) # downloaded_paths = response.download(arguments)
    # print("\n\n")
    files_modified_after_test_started = [name for name in os.listdir(output_folder_path) if os.path.isfile(os.path.join(output_folder_path, name)) and os.path.getmtime(os.path.join(output_folder_path, name)) > start_time]
    end_amount_of_files_in_output_folder = len(files_modified_after_test_started)
    print(f"Files downloaded by test {__name__}:")
    for file in files_modified_after_test_started:
        print(os.path.join(output_folder_path, file))


    # assert end_amount_of_files_in_output_folder - start_amount_of_files_in_output_folder == argumnets['limit']
    # assert end_amount_of_files_in_output_folder == arguments['limit']

    # print(f"Cleaning up all files downloaded by test {__name__}...")
    # for file in files_modified_after_test_started:
    #     if silent_remove_of_file(os.path.join(output_folder_path, file)):
    #         print(f"Deleted {os.path.join(output_folder_path, file)}")
    #     else:
    #         print(f"Failed to delete {os.path.join(output_folder_path, file)}")

# test_download_images_to_default_location("github")


# accepts each block and its number, the number helps to identify the block number
def processBlock(block, i):
    # print(block)
    heading = block['heading']
    bold = block['bold']
    italic = block['italic']
    underline = block['underline']
    hyperlink = block['hyperlink']
    paraContent = block['paraContent']

    summarized_text = summarize(paraContent, 0.34)

    # print(heading)
    # print(paraContent)
    # print(summarized_text, "\n")
    download_images(heading, i)

    print(italic, underline, hyperlink)
    for x in bold:
        for y in x:
            download_images(y, i)
    for x in italic:
        for y in x:
            download_images(y, i)
    for x in underline:
        for y in x:
            download_images(y, i)

    # hyperlink is under maintanence
    # for x in hyperlink:
    #     for y in x:
    #         download_images(y, i)

    # download_images(paraContent, i)

'''     
    {
    heading: "first heading", 
    subtitle: "subtitle", 
    paraContent: "following paragraph", 
    bold:[["bold1", "bold2", "bold3"], ["bold1", "bold2", "bold3"], ["bold1", "bold2", "bold3"]],
    italic:[["italic1", "italic2", "italic3"], ["italic1", "italic2", "italic3"]],
    underline:[["underline1", "underline2", "underline3"], ["underline1", "underline2", "underline3"], ["underline1", "underline2", "underline3"]],
    hyperlink:[["link1", "link1", "link1", "link1"], ["link1", "link1", "link1", "link1"], ["link1", "link1", "link1", "link1"]]
    }        
      
'''