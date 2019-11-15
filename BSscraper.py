
from bs4 import BeautifulSoup
import os
import fnmatch


path = r'c:\Users\jsellars\Downloads\websites\member'
os.chdir(path)
total_files = len(fnmatch.filter(os.listdir(path), '*.html'))
total_num = total_files
p = 0
file_list = os.listdir()

while p < total_num:
    for p in range(1):
        if p == total_num:
            break
        elif p < total_num:
            #print("File ",p," of ",total_num," recorded.")
            #p = p + 1
            for name in file_list:
                if name.endswith(".html"):  # You could also add "and i.startswith('f')
                    with open(name, 'r', encoding="utf8") as f:
                        for contents in f:
                            contents = f.read()
                            soup = BeautifulSoup(contents, 'html.parser')
                            print("File ",p," of ",total_num," recorded.")
                            p = p + 1
                            try:
                                business = soup.find(id="mn-member-name-nologo").get_text(strip=True, separator=',').split(',')[0]
                            except:
                                business = " "
                            try:
                                address1 = soup.find('div', class_=['mn-address1']).get_text(strip=True, separator=',')
                            except:
                                address1 = " "
                            try:
                                address2 = soup.find('div', class_=['mn-address2']).get_text(strip=True, separator=',')
                            except:
                                address2 = " "
                            try:
                                city_prov = soup.find('span', class_=['mn-cityspan']).get_text(strip=True, separator=',')
                            except:
                                city_prov = " "
                            try:
                                state = soup.find('span', class_=['mn-stspan']).get_text(strip=True, separator=',')
                            except:
                                state = " "
                            try:
                                zipcode = soup.find('span', class_=['mn-zipspan']).get_text(strip=True, separator=',')
                            except:
                                zipcode = " "
                            try:
                                member_name = soup.find('div', class_=['mn-member-repname']).get_text(strip=True, separator=',').split(',')[0]
                            except:
                                member_name = " "
                            try:
                                member_title = soup.find('div', class_=['mn-member-reptitle']).get_text(strip=True, separator=',').split(',')[0]
                            except:
                                member_title = " "
                            try:
                                category = soup.find('ul', class_=['mn-member-cats']).get_text(strip=True, separator='|').split(',')[0]
                            except:
                                member_title = " "
                                
                            with open('output.txt', 'a+') as file:
                                file.write('{0},{1},{2},{3},{4},{5},{6},{7},{8}\n'.format(business,member_name,member_title,category,address1,address2,city_prov,state,zipcode))
                    f.close()
             
print("All done ",total_files," recorded to output.txt")
exit()

    