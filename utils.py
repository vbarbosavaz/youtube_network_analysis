import pandas as pd
import re

def get_urls(colname, clipboard, display, df=None, file=None):
    """
    how to use : urls = get_urls("Ordre", False, True, None, "youtube-a-lecole-hutin.csv")
    """
    if file:
        df = pd.read_csv(file, delimiter=";", encoding='utf-8')

    mylist = df[colname].tolist()
    mystring = ','.join(map(str, mylist)) 
    df=pd.DataFrame([mystring])

    result = df.loc[:,0].tolist()
    
    if clipboard:
        df.to_clipboard(index=False,header=False)
    if display:
        print(result)
    return result

def get_id(url):
    """
    Get the channel's YouTube identifier.
    input: https://www.youtube.com/channel/UCtqICqGbPSbTN09K1_7VZ3Q
    output: UCtqICqGbPSbTN09K1_7VZ3Q
    """
    cleaned_url = re.sub(r"https://www.youtube.com/channel/", '', url)
    cleaned_url = re.sub(r"https://www.youtube.com/user/", '', cleaned_url)
    cleaned_url = re.sub(r"/.*", '', cleaned_url)
    
    return cleaned_url