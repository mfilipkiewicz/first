#kilka adrsow url i bedzie po nich iterowal, zczyta sadres sreony i zliczy wystapienia jakis slow, na jakiej stronie jaki wyraz i ile ich
import requests
import json
URL1 = "https://wp.pl"
URL2 = "https://onet.pl"
URL3 = "https://issues.apache.org/jira/rest/api/2/issue/ZOOKEEPER-2613"

def count_words_on_website(url, words):

    for k in url:
        r = requests.get(k, verify=False)
        tab=r.text
        for i in words:
            if i in tab:
                print(i)
                liczba = r.text.count(i, 0, len(r.text))
                print("strona ", k, " ilosc slowa", i, ": ", liczba)
            else:
                print("nie ma Slowa ", i," na stronie ", k)
dict = ["Trump", "Merkel"]
URLS = [URL1, URL2]
count_words_on_website(URLS, dict)
#count_words_on_website(URL2, dict)
