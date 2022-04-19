from google_images_download import google_images_download
import os, errno
import time
from summary import summarize
from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch
import spacy

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
def download_images(keyword):
    start_time = time.time()
    arguments = {
        "keywords": '"'+keyword+'"', # the keyword to search
        "limit": 5,
        "print_urls": False,
        'output_directory':'static',
        # "image_directory":str(i), # the directory to which images are downloaded under downloads/
        "image_directory":"downloads", # the directory to which images are downloaded under downloads/
        "format":"jpg"
    }
    # try:
    #     temp = arguments['output_folder']
    # except KeyError:
    #     pass
    # else:
    #     assert False, "This test checks download to default location yet an output folder was provided"

    output_folder_path = os.path.join(os.path.realpath('.'), 
                'static\\downloads\\') 
                # '{}'.format(i))
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
    i=1
    for file in files_modified_after_test_started:        
        i += 1
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

j = 0
# accepts each block and its number, the number helps to identify the block number
def processBlock(block):
    # print(block)
    heading = block['heading']
    # bold = block['bold']
    # italic = block['italic']
    # underline = block['underline']
    # hyperlink = block['hyperlink']
    paraContent = block['paraContent']

    download_images(heading)

    nouns_found_are = findNouns(paraContent)

    # remove the duplicates from nouns_found_are
    a = 0
    temp = []
    for a in nouns_found_are:
        if a[0] not in temp:
            temp.append(a[0])
    
    print(temp)
    nouns_found = []
    for a in temp:
        for b in nouns_found_are:
            if a == b[0]:
                nouns_found.append(b)
                break
    
    
    nouns_str = ""
    print("nouns found are: ", nouns_found)

    # below code will combine adjacent nouns and will use it to download images
    x = 0
    while x < len(nouns_found)-1:
        if ((nouns_found[x])[1])+1 == ((nouns_found[x+1])[1]):
            nouns_str = (nouns_found[x])[0] + " "+ (nouns_found[x+1])[0]
            download_images(nouns_str)
            # print("something ******************************")
            x += 2
        else:
            download_images((nouns_found[x])[0]) 
            x += 1


    # print(nouns_str)
    # summarized_text = summarize(paraContent, 0.34)

    # print(heading)
    # print(paraContent)
    # print(summarized_text, "\n")
    # summarize_content(paraContent)

    global j
    files = os.listdir('static/downloads/')
    for singleFile in files:
        # extension has not been added, but it's still working!!
        os.rename('static/downloads/'+ singleFile, 'static/downloads/'+str(j)+'.jpg')
        j += 1

    # download_images(summarized_text, i)

    # print(italic, underline, hyperlink)
    # for x in bold:
    #     for y in x: 
    #         download_images(y, i)
    # for x in italic:
    #     for y in x:
    #         download_images(y, i)
    # for x in underline:
    #     for y in x:
    #         download_images(y, i)

    # hyperlink is under maintanence
    # for x in hyperlink:
    #     for y in x:
    #         download_images(y, i)

    # download_images(paraContent, i)


def findNouns(para):
    nlp = spacy.load("en_core_web_sm")
    # returns a document of object
    doc = nlp(para)

    nouns = []
    # checking if it is a noun or not
    m = 1
    for x in doc:
        if(x.tag_ == 'NNP'):
            nouns.append([x.text, m])
        m += 1
    return nouns

def summarize_content(para):
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"
    summarizer = pipeline("summarization")
    summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")

    summary = summarizer(para, max_length=50, min_length=5, do_sample=False)[0]['summary_text']
    return summary
    


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

# pip install torch==1.8.2+cu102 torchvision==0.9.2+cu102 torchaudio===0.8.2 -f https://download.pytorch.org/whl/lts/1.8/torch_lts.html