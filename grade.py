import sqlite3
import os.path

def init_db(cur):
    query = """
    CREATE TABLE grades (
        Mata_Pel VARCHAR(255),
        UH1 DOUBLE,
        UH2 DOUBLE,
        UH3 DOUBLE,
        PTS DOUBLE,
        PAT DOUBLE
    );
    """
    cur.execute(query)

def query_db(query):
    cur.execute(query)
    result = cur.fetchall()
    con.commit()
    return result

if not (os.path.isfile("grade.db")):
    con = sqlite3.connect('grade.db')
    cur = con.cursor()
    init_db(cur)
    
con = sqlite3.connect('grade.db')
cur = con.cursor()

input_mapel = (input("Masukan mapel: \n> ")).lower()

nilai = ["UH1", "UH2", "UH3", "PTS", "PAT"]
list_nilai = []

for mapel in nilai:
    input_nilai = float(input(f"input nilai nigger {mapel}: \n> "))
    list_nilai.append(input_nilai)

print(input_mapel)
print(list_nilai)

query_nilai = f"""
INSERT INTO grades (
    Mata_Pel, UH1, UH2, UH3, PTS, PAT
    ) 
    VALUES
    ('{input_mapel}', {list_nilai[0]}, {list_nilai[1]}, {list_nilai[2]}, {list_nilai[3]}, {list_nilai[4]});
"""

res = query_db(query_nilai)
print(res)