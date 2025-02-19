import os

def save_file_to_csv(data, file_name, folder='csv_files_for_dashboard'):
    if not os.path.exists(folder):
        os.makedirs(folder)

    file_path = os.path.join(folder, file_name)
    data.to_csv(file_path, index=False)
    print(f'File {file_name} saved to {file_path}')