import mysql.connector as m

def get_data_fromTable(tablename,DatabaseSelected):
    demodb=m.connect(host="localhost",user="root",passwd="root@123",database=DatabaseSelected)
    democursor=demodb.cursor()

    Records=[]
    democursor.execute(f"select* from {tablename}")
    for j in democursor:
        Records.append(list(j[1:]))
    
    return Records

def getAllTableDataFromDatabase(Database):
    #use database to get all the values
    database_sel='alok'
    WorkTableData=get_data_fromTable('work_todo',database_sel)
    SkillTableData=get_data_fromTable('skill_todo',database_sel)
    PersonalTableData=get_data_fromTable('personal_todo',database_sel)
    ShoppingTableData=get_data_fromTable('shopping_todo',database_sel)
    alldata = {
        'Work': WorkTableData,
        'Skill': SkillTableData,
        'Personal': PersonalTableData,
        'Shopping': ShoppingTableData,
    }
    return alldata


def AddDataInDataBase(formdatainDict, DatabaseSelected):
    demodb = m.connect(host="localhost", user="root", passwd="root@123", database=DatabaseSelected)
    democursor = demodb.cursor()

    # Get the table name from the form data
    table_name = formdatainDict.get('Category', '')

    # Ensure that the table name is not empty
    if not table_name:
        print("Error: Table name is missing.")
        return

    # Remove the 'Category' key from the dictionary since it's not a column
    del formdatainDict['Category']

    # Construct the SQL INSERT statement dynamically
    columns = ', '.join(formdatainDict.keys())
    values_template = ', '.join(['%s'] * len(formdatainDict))
    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({values_template})"

    # Get values from the formdatainDict dictionary
    values = tuple(formdatainDict.values())

    try:
        democursor.execute(insert_query, values)
        demodb.commit()
        print(f"Data added to the {table_name} table in {DatabaseSelected} database.")
    except m.Error as err:
        demodb.rollback()
        print(f"Error: {err}")
    finally:
        democursor.close()
        demodb.close()

def DeleteDataInDataBase(dataToDelete, DatabaseSelected):
    demodb = m.connect(host="localhost", user="root", passwd="root@123", database=DatabaseSelected)
    democursor = demodb.cursor()

    for table_name, task_list in dataToDelete.items():
        print(f"Deleting data from {table_name} with tasks: {task_list}")

        # Construct the SQL DELETE statement
        # Use single quotes for string values
        quoted_tasks = ', '.join([f"'{task}'" for task in task_list])
        delete_query = f"DELETE FROM {table_name} WHERE task IN ({quoted_tasks})"
        
        try:
            democursor.execute(delete_query)
            demodb.commit()
            print(f"Deleted data from {table_name} with tasks: {task_list}")
        except m.Error as err:
            demodb.rollback()
            print(f"Error: {err}")

    democursor.close()
    demodb.close()


def DeleteDataInDataBas(dataToDelete, DatabaseSelected):
    demodb = m.connect(host="localhost", user="root", passwd="root@123", database=DatabaseSelected)
    democursor = demodb.cursor()

    for table_name, id_list in dataToDelete.items:
        print(f"Deleting data from {table_name} with IDs: {id_list}")

        # Construct the SQL DELETE statement
        delete_query = f"DELETE FROM {table_name} WHERE id IN ({', '.join(map(str, id_list))})"
        
        try:
            democursor.execute(delete_query)
            demodb.commit()
            print(f"Deleted data from {table_name} with IDs: {id_list}")
        except m.Error as err:
            demodb.rollback()
            print(f"Error: {err}")

    democursor.close()
    demodb.close()

