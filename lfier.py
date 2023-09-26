import requests
import sys 

def banner():
    with open("banner.txt") as banner:
        print(banner.read())

def lfier(url):

    print()
    print("Tap Ctrl + C to stop the program")
    print()
    print("Checking for LFI vulnerability in " + url + "\n")

    vuln = False
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}
    

    #Paths from PayloadsAllTheThings
    with open("paths.txt") as paths_to_check:
        
        for path in paths_to_check:
            
            full_url = url + path.strip()                   

            response = requests.get(full_url, headers=headers) 

            if "root:x:" in response.text:
                print("[+] The url " + full_url + " is vulnerable to LFI.\n")
                vuln = True
    
    if not vuln:
        print("[-] The URL is not vulnerable to LFI.\n")
        



if __name__ == "__main__":
    banner()
    print()
    print()
    print("Insert the URL of the target with the following format: http://www.example.com/index.php?page=")
    print("\n")


    try:
        target_url = input("URL:  ")
        lfier(target_url)

    except KeyboardInterrupt:
        print("\n")
        print("Exiting...")
        sys.exit(0)



    
