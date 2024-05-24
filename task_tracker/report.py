import pandas as pd

def generate_report(tasks, output_file):
    df = pd.DataFrame(tasks, columns=['ID', 'Title', 'Description', 'Start Date', 'Deadline', 'Status', 'Priority', 'Payment'])
    total_payment = df['Payment'].sum()
    df.loc['Total'] = ['', '', '', '', '', '', 'Total Payment', total_payment]
    df.to_excel(output_file, index=False)
