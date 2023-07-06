import datetime
import wikipedia

def time():
    strt = datetime.datetime.now().strftime("%H:%M")
    return strt


def wiki(query):
    
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=1)
    
    print(results)
    return results


