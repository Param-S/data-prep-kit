import os
import tempfile
import subprocess

def write_content(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)

def find_dead_code(file_path):
    command = f"vulture {file_path} --min-confidence 100".split()
    execution_result=subprocess.run(command, 
                       capture_output=True
                      )
    if execution_result.stdout:
        return True
    return False

def has_dead_code(filename, content):
    with tempfile.TemporaryDirectory() as tmp:
        file_path = os.path.join(tmp, filename)
        write_content(file_path, content)
        return find_dead_code(file_path)  

def dead_code_filter(df):
    import pandas as pd
    dead_code_column_list =  [has_dead_code(os.path.basename(x[0]), x[1]) for x in zip(df.file_name.to_list(), df.contents.to_list())]
    df_dead_code_column = pd.DataFrame.from_dict( {'has_dead_code': dead_code_column_list})
    modified_df = df.join(df_dead_code_column)
    return modified_df

