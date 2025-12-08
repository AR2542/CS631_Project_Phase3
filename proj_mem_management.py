from queries import QUERIES_1


def query_member_proj():
    # custom_query = input("If you would like to enter a custom query, type it here or press Enter to use the default: ").strip()
    choices = dict(enumerate(QUERIES_1.keys()))
    print("Select one from the following query choices")
    for key, choice in choices.items():
        print(f"{key+1}. {choice}")
    sel = int(input("Your selection: ")) 
    query = QUERIES_1[choices[sel-1]]
    id = []
    if sel in (1, 2, 3, 4):  # Compare integers, not strings
        
        new = input("Specific MemberID or ProjectID or GrantID you are looking for? (type 'exit' when done): ")
        while new != 'exit':
            id.append(int(new))
            new = input("Specific MemberID or ProjectID or GrantID you are looking for? (type 'exit' when done): ")
    if len(id) == 0 and sel == 2:  # Integer comparison
        query = """SELECT * FROM project;"""
    elif len(id) == 0 and sel == 1:  # Integer comparison
        query = """SELECT * FROM Lab_member;"""
    elif len(id) == 0 and sel == 3:
        id = [0]
    elif len(id) == 0 and sel == 4:
        id = [2000]

    if sel == 6:  # Integer comparison
        Member_ID = int(input("Enter new Member ID: "))
        Member_Name = input("Enter new Member Name: ")
        Member_Type = input("Enter new Member Type: ")
        Join_Date = input("Enter Join Date(yyyy-mm-dd): ")
        return query, [Member_ID, Member_Name, Member_Type, Join_Date], sel
    if sel == 7:  # Integer comparison
        print("Need to be done")

    return query, id, sel
    

# placeholder = '%s'    
# print(query_member_proj("member").replace('{placeholder}',placeholder))