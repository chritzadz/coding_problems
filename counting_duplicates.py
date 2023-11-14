def duplicate_count(text):
    lowercased = text.lower()
    listed = list(lowercased)
    remove_duplicate = list(set(listed))
    length_list = len(listed)
    legth_list_set = len(remove_duplicate)
    
    
    return 