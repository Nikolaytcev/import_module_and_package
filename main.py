from datetime import datetime

import wikipediaapi

from application.salary import calculate_salary

from application.db.people import Employee


class Wikipedia:
    def __init__(self, wiki):
        self.wiki = wiki
        
    def get_page(self, title):
        try:
            return self.wiki.page(f'{title}').fullurl
        except:
            return "Page don't found"
    
    
def main():
    now = datetime.now()
    print(f'Today is {now.year}-{now.month}-{now.day}')
    name = input('Insert name: ')
    print(f"{Employee(name).get_employees()}, {calculate_salary(name)}")
    
    wiki = wikipediaapi.Wikipedia('en')
    print(Wikipedia(wiki).get_page(input('Insert title: ')))


if __name__ == '__main__':
    main()
