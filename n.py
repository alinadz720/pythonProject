import pyodbc
conn = pyodbc.connect('Driver={SQL Server Native Client 11.0};'
                      'Server=DESKTOP-6783BGC\MSSQLSERVER007;'
                      'Database=ALINA_PYTHON;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()



cursor.execute('SELECT * FROM ALINA_PYTHON.dbo.User')

cursor.execute('''
                INSERT INTO ALINA_PYTHON.dbo.User (id, username, firstname, lastname, email, password, phone)
                VALUES
                (1, 'user1', 'Firstname1', 'Lastname1', '1email@gmail.com', '12345678', '0910345628'),
                (2, 'user2', 'Firstname2', 'Lastname2', '2email@gmail.com', '12325278', '0920347238'),
                (3, 'user3', 'Firstname3', 'Lastname3', '3email@gmail.com', '12545678', '0937395628')

                ''')
conn.commit()




cursor.execute('''
                INSERT INTO ALINA_PYTHON.dbo.Product (id, name, status)
                VALUES
                (1, 'Phone', 'available'),
                (2, 'TV', 'available'),
                (3, 'Notebook', 'available'),
                (4, 'MidiKeyboard', 'available'),
                (5, 'Monitor', 'available'),
                (6, 'PC', 'available'),
                (7, 'Headphone', 'available'),
                (8, 'Ebook', 'available')

                ''')
conn.commit()




cursor.execute('SELECT * FROM ALINA_PYTHON.dbo.Order')

cursor.execute('''
                INSERT INTO ALINA_PYTHON.dbo.Order (id, userId, productId, status, is_complete)
                VALUES
                (1, 1, 1, 'placed', 1),
                (2, 2, 3, 'placed', 1)
                ''')
conn.commit()

