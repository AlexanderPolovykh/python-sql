import psycopg2

# Создаем соединение с базой
# hexlet_test - Имя базы данных
try:
    conn = psycopg2.connect('postgresql://polovykh:123@localhost:5432/hexlet')
except:
    print('Can`t establish connection to database')

sql = "CREATE TABLE sql_users (id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY, username VARCHAR(255), phone VARCHAR(255))"
# Запрос выполняется через создание объекта курсора
cursor = conn.cursor()
cursor.execute(sql)
cursor.close() # в конце закрывается

sql2 = "INSERT INTO sql_users (username, phone) VALUES ('tommy', '123456789');"
cursor = conn.cursor()
cursor.execute(sql2)
cursor.close()

sql3 = "SELECT * FROM sql_users;"
cursor = conn.cursor()
# Указатель на набор данных в памяти СУБД
cursor.execute(sql3)
for row in cursor:
    print(row)
cursor.close()

conn.commit() # Коммитим, т.е. сохраняем измения в БД
conn.close() # Соединение нужно закрыть
