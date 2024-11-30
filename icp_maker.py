def icp_reader():
    with open('basic_info.md', 'r', encoding='utf-8') as file:
        icp_info = file.read()
    return icp_info