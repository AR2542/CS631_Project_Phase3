import mysql.connector
from proj_mem_management import query_member_proj

def execute_query(query, id):
    """Execute a SQL query and display results."""
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#Subho1062*",
            database="research_lab"
        )

        if conn.is_connected():
            print("Connected to the Research_Lab database\n")
            
            cursor = conn.cursor()
            if not id:
                cursor.execute(query)
            else:
                # Create placeholders dynamically: %s, %s, %s
                placeholder = ', '.join(['%s'] * len(id))
                query = query.replace('{placeholder}',placeholder)
                cursor.execute(query, id)
            
            # Check if the query returns results (SELECT, SHOW, DESC, EXPLAIN, etc.)
            if cursor.description:
                results = cursor.fetchall()
                
                # Get column names
                column_names = [desc[0] for desc in cursor.description]
                
                # Print column headers
                print(" | ".join(column_names))
                print("-" * (len(" | ".join(column_names))))
                
                # Print rows
                if results:
                    for row in results:
                        print(" | ".join(str(value) if value is not None else 'NULL' for value in row))
                    print(f"\n{len(results)} row(s) returned.")
                else:
                    print("No results found.")
            else:
                # For INSERT, UPDATE, DELETE, CREATE, DROP, ALTER queries
                conn.commit()
                print(f"Query executed successfully. {cursor.rowcount} row(s) affected.")
            
            cursor.close()
        else:
            print("Failed to connect to the database")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        try:
            if conn.is_connected():
                conn.close()
                print("\nConnection closed")
        except NameError:
            pass

def main():
    """Main function to run queries interactively."""
    print("=" * 60)
    print("Research_Lab Database Query Interface")
    print("=" * 60)
    
    while True:
        print("\nMain Menu:")
        print("1. PROJECT AND MEMBER MANAGEMENT")    
        print("2. EQUIPEMENT USAGE TRACKING")    
        print("3. GRANT AND PUBLICATION REPORTING")    
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        match choice:
            case '1':
                print("\nYou are in PROJECT AND MEMBER MANAGEMENT")
                print("What would you like to do?")

                query, id, sel = query_member_proj()
                if query:
                    execute_query(query, id)
                else:
                    print("Going back to main menu.")
            
            case '2':
                # Add equipment usage tracking queries here
                print("\nEquipment Usage Tracking - Not implemented yet")
            
            case '3':
                # Add grant and publication reporting queries here
                print("\nGrant and Publication Reporting - Not implemented yet")
            
            case '4':
                print("\nExiting. Goodbye!")
                break
            
            case _:
                print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()