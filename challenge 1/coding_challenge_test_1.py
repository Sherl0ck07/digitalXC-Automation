import pandas as pd
import re

def extract_group_counts(input_file, output_file):
    df = pd.read_excel(input_file)
    
    pattern = re.compile(r"<I>(.*?)</I>")
    
    group_counts = {}
    
    for comment in df['Additional comments'].dropna():
        matches = pattern.findall(comment)
        for match in matches:
            groups = [g.strip() for g in match.split(',')]
            for group in groups:
                group_counts[group] = group_counts.get(group, 0) + 1
    
    result_df = pd.DataFrame(list(group_counts.items()), columns=['Group Name', 'Number of Occurrence'])
    
    result_df.to_csv(output_file, index=False)
    
    return result_df

extract_group_counts('coding challenge test (1).xlsx', 'output.csv')
