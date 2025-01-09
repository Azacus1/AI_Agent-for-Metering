import camelot

def extract_tables_from_pdf(file_path):
    tables = camelot.read_pdf(file_path, pages='all', flavor='stream')  # Use stream flavor for loose tables
    return [table.df for table in tables]  # Convert tables to DataFrames
