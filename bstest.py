
from bs4 import BeautifulSoup
import os

#Path = r"c:\Users\jsellars\Downloads\websites\chamber\list\member"
os.chdir(r"c:\Users\jsellars\Downloads\websites\chamber\list\member")
#filelist = os.listdir(Path)
for i in os.listdir():
    if i.endswith(".html"):  # You could also add "and i.startswith('f')
        with open(i, 'r', encoding="utf8") as f:
            for contents in f:
                contents = f.read()
                #contents = " ".join(contents.split())
                #contents.replace('\n','')
                
            soup = BeautifulSoup(contents, 'html.parser')
            
            member_area = soup.find('div', class_=['mn-section-content']).get_text(strip=True, separator=', ')#.rsplit(', ', 1)
            
            #business = soup.find(id="mn-member-name-nologo").get_text(strip=True, separator=',')
            
            #address = soup.find('div', class_=['mn-member-basicinfo']).get_text(strip=True, separator=',')
            
            #member_name = soup.find('div', class_=['mn-member-repname']).get_text(strip=True, separator=',')
            
            #member_title = soup.find('div', class_=['mn-member-reptitle']).get_text(strip=True, separator=',')
                
            with open('output.txt', 'a+') as file:
                file.write('{0},\n'.format(member_area))
                
            #print('{0},{1},{2},{3}\n'.format(member_name,member_title,business,address))                               
            #print('{0},'.format(member_area)) 
            f.close()
            if f.closed == True:
                print("File is Closed.")
            elif f.closed == False:
                print("File is still open!")
    
    
    