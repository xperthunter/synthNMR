import sqlite3

def dbinit(dbname, projectname, nimgs, imgsize, gd, limits):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    
    c.execute("CREATE TABLE projects (project_name TEXT, nimgs INT, imgsize INT, grid_density INT, limits TEXT)")
    conn.commit()
    inserter = [(projectname, nimgs, imgsize, gd, limits)]
    c.executemany("INSERT INTO projects VALUES (?, ?, ?, ?, ?)", inserter)
    conn.commit()
    conn.close()

def db_proj_update(dbname, projectname, nimgs, imgsize, gd, limits):
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    
    inserter = [(projectname, nimgs, imgsize, gd, limits)]
    c.executemany("INSERT INTO projects VALUES (?, ?, ?, ?, ?)", inserter)
    conn.commit()
    conn.close()
