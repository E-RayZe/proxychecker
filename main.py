import request 
with open("vald_proxies.txt","r") as f:
    proxies=f.read().split("\n")
    
#Enter site (http)also target
site_to_check=["XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"]

counter=0
for site in site_to_check:
    try:
        print(f"using the proxy:{proxies[counter]}")
        res = request.get(site,proxies={"http":proxies[counter],
                                        "https":proxies[counter]})
        print(res.status_code)
    except:
        print("Failed")